import React, { useState } from 'react';

interface Props {
  onSwitch: () => void;
}

const SignUpForm: React.FC<Props> = ({ onSwitch }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirm, setConfirm] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (password !== confirm) return alert("Passwords do not match");

    const response = await fetch('http://localhost:8000/auth/signup', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password, name: email })
    });

    const result = await response.json();
    if (!response.ok) {
      alert(result.detail || 'Signup failed');
      return;
    }
    console.log('Signup Success');
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
      <input
        type="password"
        placeholder="Confirm Password"
        value={confirm}
        onChange={(e) => setConfirm(e.target.value)}
        className="border border-gray-300 rounded px-4 py-2"
        required
      />
      <button type="submit" className="bg-[#8AA098] text-white py-2 rounded">Sign Up</button>
      <p className="text-sm text-center text-gray-600">
        Already have an account? <button type="button" className="underline" onClick={onSwitch}>Sign In</button>
      </p>
    </form>
  );
};

export default SignUpForm;
