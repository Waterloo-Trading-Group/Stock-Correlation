import './App.css';
import axios from 'axios';
import React, { useState } from 'react';
import { ChakraProvider } from '@chakra-ui/react'
import { Button } from '@chakra-ui/react'
import { Input } from '@chakra-ui/react'
// createa another function to get the data from the API

function App() {
  const [kendalCorrelation, setKCorrelation] = useState(0);
  const [pearsonCorrelation, setPCorrelation] = useState(0);
  const [spearmanCorrelation, setSCorrelation] = useState(0);
  const [stock1, setStock1] = useState('');
  const [stock2, setStock2] = useState('');

  async function getData(stock1, stock2) {
  
    axios.get('http://127.0.0.1:8000/stock_correlation/' + stock1 + '/' + stock2)
    .then((response) => {
      const data = response.data;
      const kcorrelation = data['Kendall'];
      const pcorrelation = data['Pearson'];
      const scorrelation = data['Spearman'];
      setKCorrelation(kcorrelation);
      setPCorrelation(pcorrelation);
      setSCorrelation(scorrelation);
      console.log(data);
    })
    .catch((error) => {
      console.log(error);
    });
  }

  return (
    <ChakraProvider>
      <div className="App">
        <Input htmlSize={8} width='auto'  type="text" placeholder='Stock 1' onChange={(e) => setStock1(e.target.value)} />
        <Input htmlSize={8} width='auto'  type="text" placeholder='Stock 2' onChange={(e) => setStock2(e.target.value)} />
        <Button onClick={() => getData(stock1, stock2)}>Get Data</Button>
        <p>Kendal Correlation: {kendalCorrelation}</p>
        <p>Pearson Correlation: {pearsonCorrelation}</p>
        <p>Spearman Correlation: {spearmanCorrelation}</p>
      </div>
    </ChakraProvider>

  );
}

export default App;
