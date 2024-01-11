import React from 'react';
import logo from './logo.svg';
import './App.css';
import Header from "./components/Header";
import {Grid, GridItem} from "@chakra-ui/react";
import Income from "./components/Income";

function App() {
  return (
    <div className="App">
        <Grid
            templateAreas={`"header header"
                  "nav main"
                  "nav main"`}
            gridTemplateColumns={'auto 1fr'}
            h='200px'
            gap='1'

        >
            <GridItem pl='2'area={'header'}>
                <Header />
            </GridItem>
            <GridItem pl='2'  area={'nav'}>
                <Income/>
            </GridItem>
            <GridItem pl='2' bg='green.300' area={'main'}>
                Main
            </GridItem>
        </Grid>
    </div>
  );
}

export default App;
