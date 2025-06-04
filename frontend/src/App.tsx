/*export default function App() {
  return <div style={{ background: 'green', height: '100vh' }}>TEST WORKS ✅</div>;
}*/

import { useEffect, useState } from 'react';
import SplashScreen from './components/SplashScreen';
import AuthPage from './components/pages/AuthPage';

function App() {
  const [showSplash, setShowSplash] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => {
      setShowSplash(false);
    }, 2500); // 2.5 seconds for splash screen

    return () => clearTimeout(timer);
  }, []);

  return showSplash ? <SplashScreen /> : <AuthPage />;
}

export default App;
