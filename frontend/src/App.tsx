import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ThemeProvider } from '@mui/material/styles';
import { createTheme } from '@mui/material';
import { Toaster } from 'react-hot-toast';
import { Chat } from './pages/Chat';

const queryClient = new QueryClient();
const theme = createTheme();

function App() {
    return (
        <QueryClientProvider client={queryClient}>
            <ThemeProvider theme={theme}>
                <Router>
                    <Routes>
                        <Route path="/chat" element={<Chat />} />
                    </Routes>
                </Router>
                <Toaster position="top-right" />
            </ThemeProvider>
        </QueryClientProvider>
    );
}

export default App;