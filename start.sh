echo "Cloning Repo, Please Wait..."
git clone https://github.com/casperTeam/never1.git /never
echo "Installing Requirements..."
cd /never1
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 main.py
