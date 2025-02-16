import { useState } from 'react';
import { Box, TextField, Button, Paper, Typography, CircularProgress } from '@mui/material';
import { useMutation } from '@tanstack/react-query';
import axios from 'axios';

interface Message {
    question: string;
    answer: string;
}

export const Chat = () => {
    const [question, setQuestion] = useState('');
    const [messages, setMessages] = useState<Message[]>([]);

    const askQuestion = useMutation({
        mutationFn: async (question: string) => {
            const response = await axios.post('http://localhost:8000/api/llm/ask/', {
                question
            }, {
                withCredentials: true
            });
            return response.data;
        },
        onSuccess: (data) => {
            setMessages(prev => [...prev, { question, answer: data.steps[2].generate_answer.answer }]);
            setQuestion('');
        }
    });

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (question.trim()) {
            askQuestion.mutate(question);
        }
    };

    return (
        <Box sx={{ maxWidth: 800, mx: 'auto', p: 3 }}>
            <Typography variant="h4" sx={{ mb: 4 }}>
                Chat with Buy n Large Assistant
            </Typography>

            {/* Messages Area */}
            <Paper
                sx={{
                    height: '60vh',
                    mb: 2,
                    p: 2,
                    overflowY: 'auto',
                    backgroundColor: '#f5f5f5'
                }}
            >
                {messages.map((message, index) => (
                    <Box key={index} sx={{ mb: 2 }}>
                        <Paper sx={{ p: 2, backgroundColor: '#e3f2fd', mb: 1 }}>
                            <Typography><strong>You:</strong> {message.question}</Typography>
                        </Paper>
                        <Paper sx={{ p: 2, backgroundColor: '#fff' }}>
                            <Typography><strong>Assistant:</strong> {message.answer}</Typography>
                        </Paper>
                    </Box>
                ))}
                {askQuestion.isPending && (
                    <Box display="flex" justifyContent="center" my={2}>
                        <CircularProgress />
                    </Box>
                )}
            </Paper>

            {/* Input Area */}
            <form onSubmit={handleSubmit}>
                <Box sx={{ display: 'flex', gap: 2 }}>
                    <TextField
                        fullWidth
                        value={question}
                        onChange={(e) => setQuestion(e.target.value)}
                        placeholder="Ask something about the store..."
                        disabled={askQuestion.isPending}
                    />
                    <Button
                        type="submit"
                        variant="contained"
                        disabled={askQuestion.isPending || !question.trim()}
                    >
                        Send
                    </Button>
                </Box>
            </form>
        </Box>
    );
}; 