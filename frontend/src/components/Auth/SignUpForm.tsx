import { useState } from "react";
import Eye from "@/assets/Eye.png";
import EyeOff from "@/assets/EyeOff.png";
import SignUpButton from "@/assets/SignUpButton.png";

export default function SignUpForm() {
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);

  return (
    <>
      {/* Email Field */}
      <div className="pb-[0px]">
        <label className="block text-[16px] font-poppins text-[#677363] leading-tight">
          Email address
        </label>
        <input
          type="email"
          placeholder="Enter email"
          className="w-[420px] h-[38px] border-2 border-[#D3D8D0] rounded-[5px] px-3 font-poppins text-[13px]"
        />
      </div>

      {/* Password Field */}
      <div className="pb-[0px]">
        <label className="block text-[16px] font-poppins text-[#677363] leading-tight">
          Password
        </label>
        <div className="relative w-[420px]">
          <input
            type={showPassword ? "text" : "password"}
            placeholder="Enter password"
            className="w-full h-[38px] border-2 border-[#D3D8D0] rounded-[5px] px-3 pr-10 font-poppins text-[13px]"
          />
          <img
            src={showPassword ? EyeOff : Eye}
            alt="Toggle visibility"
            onClick={() => setShowPassword(!showPassword)}
            className="absolute right-[10px] top-1/2 transform -translate-y-1/2 w-[20px] h-[20px] cursor-pointer"
          />
        </div>
      </div>

      {/* Confirm Password Field */}
      <div className="pb-[0px]">
        <label className="block text-[16px] font-poppins text-[#677363] leading-tight">
          Confirm Password
        </label>
        <div className="relative w-[420px]">
          <input
            type={showConfirmPassword ? "text" : "password"}
            placeholder="Re-enter password"
            className="w-full h-[38px] border-2 border-[#D3D8D0] rounded-[5px] px-3 pr-10 font-poppins text-[13px]"
          />
          <img
            src={showConfirmPassword ? EyeOff : Eye}
            alt="Toggle visibility"
            onClick={() => setShowConfirmPassword(!showConfirmPassword)}
            className="absolute right-[10px] top-1/2 transform -translate-y-1/2 w-[20px] h-[20px] cursor-pointer"
          />
        </div>
      </div>

      {/* Sign Up Button */}
      <div className="flex justify-center pt-[0px]">
        <img
          src={SignUpButton}
          alt="Sign Up"
          className="cursor-pointer w-[250px] h-[50px]"
        />
      </div>
    </>
  );
}