# Loada
Loada.ai

🚛 Loada.ai – AI-Powered Freight Negotiation Web App

Loada.ai is an intelligent, serverless web application that empowers truckers and freight dispatchers to evaluate and negotiate loads with data-backed insights and AI-driven guidance. Designed with real-world logistics challenges in mind, Loada combines load economics, live fuel prices, GPS-based deadhead calculations, and simulated freight market rates to help users make smart decisions fast.

💡 Features:
	• 📍 Automatic Deadhead & Load Mile Calculation using Google Maps API
	• ⛽ Fuel Cost Estimation based on truck MPG, load weight, and real-time state fuel prices (via EIA API)
	• 📈 Offer Profitability Analysis against current market rates (simulated DAT API)
	• 🤖 Loada AI Negotiator — real-time AI chat to guide truckers through broker negotiations
	• 🔐 Secure Authentication & Password Recovery using AWS Cognito
	• ☁️ Serverless Architecture powered by AWS Lambda, API Gateway, and DynamoDB
	• 📱 Responsive UI/UX optimized for mobile and desktop browsers, designed in Figma

🛠️ Built With:
	• Frontend: React.js (TypeScript)
	• Backend: Python (FastAPI)
	• Database: AWS DynamoDB (NoSQL)
	• Authentication: AWS Cognito
	• APIs:
	• Google Maps API (Geolocation, Distance Matrix)
	• EIA Fuel Price API (Diesel prices by U.S. state)
	• GPT API (AI-driven negotiation assistant)
	• Simulated DAT API (market rates)
	• Deployment: AWS Lambda, API Gateway, CloudFront
	• Design: Figma
