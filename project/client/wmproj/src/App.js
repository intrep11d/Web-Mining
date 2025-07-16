import React from 'react'
import { motion } from 'framer-motion'
import './App.css'
import BasicSelect from './BasicSelect'
import { Typewriter } from './typewriter'
import logo from './logo.png'

function App() {
  return (
    <div className="App">
      <motion.header
        className="App-header"
        initial={{ opacity: 0, y: 50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 1, ease: 'easeOut' }}
      >
        <img src={logo} alt="Logo" />
      </motion.header>
      <motion.header
        className="App-header"
        initial={{ opacity: 0, y: 50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 1, delay: 1}}
      >
        Welcome to Yumei!
      </motion.header>

      <motion.p
          initial={{ opacity: 0, y: 60 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1, delay: 1}}
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
