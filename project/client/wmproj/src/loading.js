import { motion } from "motion/react"
import './App.css'

function LoadingThreeDotsJumping() {
  const dotVariants = {
    jump: {
      y: -30,
      transition: {
        duration: 0.8,
        repeat: Infinity,
        repeatType: "mirror",
        ease: "easeInOut",
      },
    },
  }

  return (
    <div className="loading-wrapper">
      <motion.div
        animate="jump"
        transition={{ staggerChildren: -0.2, staggerDirection: -1 }}
        className="container"
      >
        <motion.div className="dot" variants={dotVariants} />
        <motion.div className="dot" variants={dotVariants} />
        <motion.div className="dot" variants={dotVariants} />
      </motion.div>

      <div className="loading-text">PDF Generating...</div>

      <StyleSheet />
    </div>
  )
}

/**
 * ==============   Styles   ================
 */
function StyleSheet() {
  return (
    <style>
      {`
        .loading-wrapper {
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          gap: 12px;
          color: #f7f7f7;
          font-family: monospace;
          font-size: 1.2rem;
          margin-top: 10px;
        }

        .container {
          display: flex;
          justify-content: center;
          align-items: center;
          gap: 10px;
        }

        .dot {
          width: 20px;
          height: 20px;
          border-radius: 50%;
          background-color: #f7f7f7ff;
          will-change: transform;
        }

        .loading-text {
          margin-top: 10px;
          text-align: center;
        }
      `}
    </style>
  )
}

export default LoadingThreeDotsJumping
