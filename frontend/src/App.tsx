import { Routes, Route } from "react-router-dom";
import SplashScreen from "./pages/SplashScreen";
import AuthForm from "./components/Auth/AuthForm";
import ForgotPasswordForm from "./components/Auth/ForgotPasswordForm";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<SplashScreen />} />
      <Route path="/auth" element={<AuthForm />} />
      <Route path="/forgot-password" element={<ForgotPasswordForm />} />
    </Routes>
  );
}