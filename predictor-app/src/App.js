import './App.css';
import React, { useState, useCallback } from 'react';
import styled from 'styled-components';
import {useSpring, animated } from 'react-spring'
import { useResizeDetector } from 'react-resize-detector';
import axios from 'axios';
import _ from 'lodash';

function App() {
  const { width, ref } = useResizeDetector();
  const [enteredText, setEnteredText] = useState("");
  const [predictedText, setPredictedText] = useState("");
  const [extended, toggle] = useState(false);

  const data = useSpring({
    width: extended ? `${width}px` : '0px'
  });

  const handleOnChange = (e) => {
    setEnteredText(e.target.value);
    callModelWrapper(e.target.value);
  };

  const callModel = (e) => {
    if (e) {
      axios({
        method: 'POST',
        url: 'http://127.0.0.1:5000/predict',
        data: {
          string: e
        }
      })
        .then(res => {
          console.log(res);
          setPredictedText(res.data.word);
        })
        .catch(error => {
          console.log("oops lmao");
        })
    } else {
      return "";
    }
  }

  const callModelWrapper = useCallback(
    _.debounce((e) => {
      callModel(e);
    },
  1000), []);

  return (
    <div className="App">
      <Main>
        <InputWrapper>
          <InputText
          style={{ width: '720px' }}
          type="text"
          placeholder="Type here..."
          value={ enteredText }
          onFocus={ e => toggle(true) }
          onBlur={ e => toggle(false) }
          onChange={ e => handleOnChange(e) }
          ref={ ref }
          />
          <AnimatedBox className="script-box" style={data} />
        </InputWrapper>
        <P>
          { predictedText }
        </P>
      </Main>
    </div>
  );
}

const Main = styled.div`
  display: block;
`;

const InputWrapper = styled.div`
  display: block;
`;

const InputText = styled.textarea`
  background: #f5fdff;
  font-family: 'Noto Serif', serif;
  font-size: 48px;
  border: none;
  outline: none;

  &::placeholder {
    color: #888
  }
`;

const AnimatedBox = styled(animated.div)`
  background: #ff6600;
  height: 4px;
`;

const P = styled.p`
  font-size: 30px;
`;

export default App;
