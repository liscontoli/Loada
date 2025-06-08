import { useNavigate } from "react-router-dom";
import AuthLogo from "@/assets/AuthLogo.png";
import LinkToReset from "@/assets/LinkToReset.png";
import BackArrow from "@/assets/BackArrow.png";

export default function ForgotPasswordForm() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-[#C7D3C0] flex items-center justify-center">
      <div className="relative bg-[#FEFEFE] w-[955px] h-[720px] rounded-[98px] shadow-[0_8px_24px_0_rgba(0,0,0,0.1)] flex flex-col items-center px-8 pt-5">
        
        {/* Back Arrow */}
        <img
          src={BackArrow}
          alt="Back"
          onClick={() => navigate("/")}
          className="absolute left-[32px] top-1/2 transform -translate-y-1/2 w-[30px] h-[30px] cursor-pointer"
        />

        {/* Logo */}
        <img
          src={AuthLogo}
          alt="Loada Logo"
          className="w-[216px] h-[216px] mt-[32px] mb-[20px]"
        />

        {/* Title */}
        <h2 className="text-[24px] font-poppins text-[#8EA29D] mb-10">
          Forgot your password?
        </h2>

        {/* Email Input */}
        <div className="w-[417px] mb-8">
          <label className="block text-[18px] font-poppins text-left text-[#8EA29D] mb-2">
            Email address
          </label>
          <input
            type="email"
            placeholder="Enter your email"
            className="w-full h-[42px] rounded-[5px] border-2 border-[#D3D8D0] px-3 font-poppins text-[16px]"
          />
        </div>

        {/* Send Link Button */}
        <div className="flex justify-center">
          <img
            src={LinkToReset}
            alt="Send Link to Reset Password"
            className="cursor-pointer w-[250px] h-[50px]"
          />
        </div>
      </div>
    </div>
  );
}