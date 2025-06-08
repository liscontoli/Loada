import { useState } from "react";
import { Link } from "react-router-dom";
import Eye from "@/assets/Eye.png";
import EyeOff from "@/assets/EyeOff.png";
import SignInButton from "@/assets/SignInButton.png";

export default function SignInForm() {
  const [showPassword, setShowPassword] = useState(false);

  return (
    <>
      {/* Email Field */}
      <div>
        <label className="block text-[18px] font-poppins text-left text-[#677363] mb-3">
          Email address
        </label>
        <input
          type="email"
          placeholder="Enter email"
          className="w-[420px] h-[42px] rounded-[5px] border-2 border-[#D3D8D0] px-3 font-poppins text-[16px]"
        />
      </div>

      {/* Password Field */}
      <div className="mt-5">
        <label className="block text-[18px] font-poppins text-left text-[#677363] mb-2">
          Password
        </label>
        <div className="relative w-[420px]">
          <input
            type={showPassword ? "text" : "password"}
            placeholder="Enter password"
            className="w-full h-[42px] rounded-[5px] border-2 border-[#D3D8D0] px-3 pr-10 font-poppins text-[16px]"
          />
          <img
            src={showPassword ? EyeOff : Eye}
            alt="Toggle visibility"
            onClick={() => setShowPassword(!showPassword)}
            className="absolute right-[10px] top-1/2 transform -translate-y-1/2 w-[20px] h-[20px] cursor-pointer"
          />
        </div>

        {/* Forgot Password Link */}
        <div className="text-right mt-1">
          <Link
            to="/forgot-password"
            className="text-[#D3D8D0] text-[12px] font-poppins cursor-pointer"
          >
            Forgot password?
          </Link>
        </div>
      </div>

      {/* Sign In Button */}
      <div className="mt-6 flex justify-center">
        <img
          src={SignInButton}
          alt="Sign In"
          className="cursor-pointer w-[250px] h-[50px]"
        />
      </div>
    </>
  );
}