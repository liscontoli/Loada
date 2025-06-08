import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import splashLogo from "@/assets/SplashScreenLogo.png";

export default function SplashScreen() {
  const navigate = useNavigate();

  useEffect(() => {
    const timer = setTimeout(() => {
      navigate("/auth");
    }, 2000);
    return () => clearTimeout(timer);
  }, [navigate]);

  return (
    <div className="flex items-center justify-center h-screen bg-[#C7D3C0] overflow-hidden">
      <img
        src={splashLogo}
        alt="Loada Logo"
        className="w-[382px] h-[382px] animate-fadeIn"
      />
    </div>
  );
}