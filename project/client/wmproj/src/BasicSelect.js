import * as React from 'react'
import Box from '@mui/material/Box'
import InputLabel from '@mui/material/InputLabel'
import MenuItem from '@mui/material/MenuItem'
import FormControl from '@mui/material/FormControl'
import Select from '@mui/material/Select'
import './App.css'
import Button from '@mui/material/Button'
import FormHelperText from '@mui/material/FormHelperText'
import axios from 'axios' 

export default function BasicSelect( {setLoading} ) {
  const [course, setCourse] = React.useState('');
  const [response, setResponse] = React.useState('');
  const [error, setError] = React.useState(false); 

  const handleChange = (event) => {
    setCourse(event.target.value);
    setError(false); 
  };

const handleGenerateClick = async () => {
  if (course === '') {
    setError(true);
    setResponse('');
    return;
  }

  setLoading(true);

  try {
    const res = await axios.post('http://localhost:5000/generate', {
      course_value: course
    });

    setResponse(res.data.message);

    const filename = res.data.filename;

    if (filename) {
      const downloadUrl = `http://localhost:5000/download/${filename}`;

      const pdfResponse = await fetch(downloadUrl);
      const blob = await pdfResponse.blob();

      const url = window.URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', filename);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      window.URL.revokeObjectURL(url);
    }
  } catch (err) {
    console.error(err);
    setResponse('Error generating content.');
  } finally {
    setLoading(false);
  }
};

  return (
    <Box sx={{ minWidth: 500 }}>
      <div className='Select'>
        <FormControl
          fullWidth
          error={error}
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
              borderColor: '#ffffff79',
              borderRadius: '100px',
              borderWidth: '2px',
            },
            '&:hover .MuiOutlinedInput-notchedOutline': {
              borderColor: '#bcbcbc4a',
            },
            '&.Mui-focused .MuiOutlinedInput-notchedOutline': {
              borderColor: '#ffffffff',
            },
          }}
        >
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
                  backgroundColor: '#1c0122',
                  color: 'white',
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
          {/* 🆕 Error message shown conditionally */}
          {error && <FormHelperText>Please select a course before generating.</FormHelperText>}
        </FormControl>

        <Button
          variant="contained"
          className='buttone'
          onClick={handleGenerateClick}
          sx={{
            backgroundColor: 'white',
            fontFamily: 'monospace',
            color: 'black',
            borderRadius: '100px',
          }}
        >
          Generate
        </Button>
      </div>
       {response && (
        <center>
          <p style={{ color: 'white', fontFamily: 'monospace', marginTop: '1rem' }}>
            {response}
          </p>
          </center>
          )}
    </Box>
  );
}