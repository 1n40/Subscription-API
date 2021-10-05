from flask import Flask, render_template, render_template, request
import threading
import time

# Defining balance and other variables
bal = 100
t1 = None
stop_threads = False



# Function to reduce balance at a specific frequency defined by user
def schedule(cre, ti, stop):
    global bal
    while 1:
        if stop():              # A stop function to stop this thread
            break
        if cre > bal:
            bal = str(bal)
            bal = "Not enough balance"
            break
        
        else:
            time.sleep(ti)
            bal -= cre
    t1.join()                   # Finally, join the thread with the main thread

    
app = Flask(__name__)

# API for root directory
@app.route('/',methods=['GET'])
def home():
    return render_template('index.htm')



# API for a buy request
@app.route('/buy',methods=['POST'])
def buy():
    data = int(request.data.decode())
    cre = 10
    global t1
    global stop_threads
    stop_threads = False
    t1 = threading.Thread(target=schedule, args=(cre,data, lambda : stop_threads, ))    # Making a thread
    if data > 50 or data < 0:
        return "ERROR!"
    else:
        t1.start()
        return str(bal)



# API to get balance 
@app.route('/balance',methods=['GET'])
def balance():
    global bal
    print(bal)
    return str(bal)


# API to cancel the subscription
@app.route('/cancel', methods=['POST'])
def cancel():
    global t1
    global stop_threads
    stop_threads = True         # Sets the flag to stop the running thread     


# API to add money to balance only 100 bucks
@app.route('/add', methods=['POST'])
def add():
    global bal
    bal += 10


if __name__=="__main__":
    app.run(debug=True)
