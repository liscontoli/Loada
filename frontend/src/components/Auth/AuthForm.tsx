import { useState } from 'react';
import SignInForm from './SignInForm';
import SignUpForm from './SignUpForm';
import AuthLogo from '../../assets/AuthLogo.png';


const AuthForm = () => {
  const [isSignIn, setIsSignIn] = useState(true);

  return (
    <div className="flex items-center justify-center min-h-screen bg-[#C7D3C0] px-4">
      <div className="bg-white p-8 rounded-[3rem] shadow-lg max-w-md w-full">
        <div className="flex justify-center mb-6">
          <img src={AuthLogo} alt="Loada Logo" className="w-28 h-28 sm:w-32 sm:h-32" />
        </div>
        <div className="flex justify-center gap-8 text-[#6B7B5D] text-lg font-medium mb-4">
          <button
            onClick={() => setIsSignIn(true)}
            className={`${isSignIn ? 'underline underline-offset-4' : 'text-gray-400'}`}
          >
            Sign In
          </button>
          <button
            onClick={() => setIsSignIn(false)}
            className={`${!isSignIn ? 'underline underline-offset-4' : 'text-gray-400'}`}
          >
            Sign Up
          </button>
        </div>
        {isSignIn ? <SignInForm onSwitch={() => setIsSignIn(false)} /> : <SignUpForm onSwitch={() => setIsSignIn(true)} />}
      </div>
    </div>
  );
};

export default AuthForm;
