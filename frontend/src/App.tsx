import { useState, useEffect } from 'react';
import SplashScreen from './components/SplashScreen';
import AuthPage from './components/pages/AuthPage';

function App() {
  const [showSplash, setShowSplash] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => setShowSplash(false), 2000); // 2 seconds
    return () => clearTimeout(timer);
  }, []);

  return showSplash ? <SplashScreen /> : <AuthPage />;
}

export default App;
