import splashLogo from '../assets/SplashScreenLogo.png';

export default function SplashScreen() {
  return (
    <div className="flex items-center justify-center h-screen bg-[#C7D3C0]">
      <img
        src={splashLogo}
        alt="Loada Logo"
        className="w-[382px] h-[382px] animate-fadeIn"
      />
    </div>
  );
}
