from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>My Python Homepage</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    text-align: center;
                    background: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);
                }

                header {
                    background-color: #333;
                    padding: 15px 30px;
                    color: white;
                    display: flex;
                    justify-content: flex-end;
                    align-items: center;
                    font-size: 18px;
                }

                .nav-links {
                    display: flex;
                    gap: 40px;
                }

                .nav-links a {
                    color: white;
                    text-decoration: none;
                    font-weight: bold;
                    transition: color 0.3s;
                }

                .nav-links a:hover {
                    color: #00e0ff;
                }

                .container {
                    margin-top: 100px;
                    animation: fadeIn 2s ease-in-out;
                }

                .btn {
                    margin-top: 30px;
                    padding: 15px 30px;
                    font-size: 18px;
                    background-color: #00bcd4;
                    color: white;
                    border: none;
                    border-radius: 25px;
                    cursor: pointer;
                    transition: transform 0.3s, background-color 0.3s;
                }

                .btn:hover {
                    background-color: #0097a7;
                    transform: scale(1.05);
                }

                @keyframes fadeIn {
                    0% { opacity: 0; transform: translateY(-20px); }
                    100% { opacity: 1; transform: translateY(0); }
                }
            </style>
        </head>
        <body>
            <header>
                <div class="nav-links">
                    <a href="/">Home</a>
                    <a href="#about">About</a>
                </div>
            </header>

            <div class="container">
                <h1>Welcome to My Hpage</h1>
                <p>This is a basic homepage using only Python and Flask.</p>
                <button class="btn">Get Started</button>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
