import os
from app import app

if __name__ == '__main__':
    os.system("start http://localhost:5000")
    app.run(debug=False)
