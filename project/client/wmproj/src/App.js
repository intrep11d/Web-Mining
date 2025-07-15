import React from 'react';
import { motion } from 'framer-motion';
import './App.css';
import BasicSelect from './BasicSelect';
import { Typewriter } from './typewriter';

function App() {
  return (
    <div className="App">
      <motion.header
        className="App-header"
        initial={{ opacity: 0, y: 50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 1, ease: 'easeOut' }}
      >
        Welcome to Yumei!
      </motion.header>

      <motion.p
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8}} // 👈 delay BasicSelect
          className="App-p"
      > 
        <Typewriter text="The social media marketing adviser for student leaders"/>
      </motion.p>

      <motion.div
        className="Select"
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, delay: 3 }} // 👈 delay BasicSelect
      >
        <BasicSelect />
      </motion.div>
    </div>
  );
}

export default App;
