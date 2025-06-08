import { useState } from "react";
import AuthLogo from "@/assets/AuthLogo.png";
import SignInForm from "./SignInForm";
import SignUpForm from "./SignUpForm";

export default function AuthForm() {
  const [isSignIn, setIsSignIn] = useState(true);

  return (
    <div className="min-h-screen bg-[#C7D3C0] flex items-center justify-center">
      <div
        className="bg-[#FEFEFE] w-[955px] h-[720px] rounded-[98px] shadow-[0_8px_24px_0_rgba(0,0,0,0.1)] flex flex-col items-center px-8 pt-5"
      >
        {/* Logo */}
        <img
          src={AuthLogo}
          alt="Loada Logo"
          className="w-[216px] h-[216px] mt-[16px] mb-[30px]"
        />

        {/* Toggle */}
        <div className="flex gap-[90px] mb-[60px]">
          <span
            onClick={() => setIsSignIn(true)}
            className={`cursor-pointer text-[24px] font-poppins ${
              isSignIn
                ? "text-[#8EA29D] border-b-3 border-[#8EA29D]"
                : "text-[#A9B8A4]"
            }`}
          >
            Sign In
          </span>
          <span
            onClick={() => setIsSignIn(false)}
            className={`cursor-pointer text-[22px] font-poppins ${
              !isSignIn
                ? "text-[#8EA29D] border-b-3 border-[#8EA29D]"
                : "text-[#A9B8A4]"
            }`}
          >
            Sign Up
          </span>
        </div>

        {/* Form */}
        <div className="w-full flex justify-center">
          <div className="w-[417px] space-y-[20px]">
            {isSignIn ? <SignInForm /> : <SignUpForm />}
          </div>
        </div>
      </div>
    </div>
  );
}