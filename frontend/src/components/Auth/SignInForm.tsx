import React, { useState } from 'react';

interface Props {
  onSwitch: () => void;
}

const SignInForm: React.FC<Props> = ({ onSwitch }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const response = await fetch('http://localhost:8000/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });

    const result = await response.json();
    if (!response.ok) {
      alert(result.detail || 'Login failed');
      return;
    }
    console.log('Token:', result);
  };

  return (
    <form onSubmit={handleSubmit} className="w-full flex flex-col gap-4 mt-4">
      <input
        type="email"
        placeholder="Email address"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        className="border border-gray-300 rounded px-4 py-2"
        required
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        className="border border-gray-300 rounded px-4 py-2"
        required
      />
      <button type="submit" className="bg-[#8AA098] text-white py-2 rounded">Sign In</button>
      <p className="text-sm text-center text-gray-600">
        Don't have an account? <button type="button" className="underline" onClick={onSwitch}>Sign Up</button>
      </p>
    </form>
  );
};

export default SignInForm;
