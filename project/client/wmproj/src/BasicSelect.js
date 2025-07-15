import * as React from 'react';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import './App.css';
import Button from '@mui/material/Button';

export default function BasicSelect() {
  const [course, setCourse] = React.useState('');

  const handleChange = (event) => {
    setCourse(event.target.value);
  };

  return (
    <Box sx={{ minWidth: 500 }}>
      <div className='Select'>
        <FormControl fullWidth
        sx={{
          
          '& .MuiInputLabel-root': {
              color: 'white', 
              fontFamily: 'monospace',
          },
          '& .MuiInputLabel-root.Mui-focused': {
              color: 'white',
          },
          '& .MuiSelect-select': {
              color: 'white', 
              fontFamily: 'monospace',
          },
          '& .MuiOutlinedInput-notchedOutline': {
              borderColor: '#ffffff79', // default border
              borderRadius: '100px',
              borderWidth: '2px',
          },
          '&:hover .MuiOutlinedInput-notchedOutline': {
              borderColor: '#bcbcbc4a', // on hover
          },
          '&.Mui-focused .MuiOutlinedInput-notchedOutline': {
              borderColor: '#ffffffff', // on focus
          },
          
        }}>
          <InputLabel id="demo-simple-select-label">Course</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            value={course}
            label="course"
            onChange={handleChange}
            MenuProps={{
              PaperProps: {
                  sx: {
                  backgroundColor: '#1c0122', // dark menu background
                  color: 'white', // white text for menu items
                  fontFamily: 'monospace',
                  },
            },
          }}
          >
            <MenuItem value={0}>💻Tech</MenuItem>
            <MenuItem value={1}>🩺Medicine</MenuItem>
            <MenuItem value={2}>🪙Business</MenuItem>
            <MenuItem value={3}>👨‍🔬Engineering</MenuItem>
            <MenuItem value={4}>✍️Journalism</MenuItem>
            <MenuItem value={5}>🎨Fine Arts</MenuItem>
            <MenuItem value={6}>🎶Music</MenuItem>
            <MenuItem value={7}>⚖️Law</MenuItem>
            <MenuItem value={8}>🏛️Architecture</MenuItem>
            <MenuItem value={9}>💡Surprise Me!</MenuItem>
          </Select>
        </FormControl>
        <Button variant="contained" className='buttone'
              sx={{
                backgroundColor: 'white',
                fontFamily: 'monospace',
                color: 'black',
                borderRadius: '100px',
                }}>
            Generate</Button>
      </div>
    </Box>
  );
}
