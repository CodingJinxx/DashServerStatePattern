import bindingtests
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
from datetime import date, datetime
from time import sleep
import threading
import logging
from serverstate import ServerState


app = dash.Dash(__name__)

app.layout = html.Div([
    bindingtests.MessageLog(
        id="log1",
        log=ServerState.log,
    )
])



def business_logic():
    counter = 0
    while True:
        counter += 1
        time = datetime.now().strftime("%HH:%MM:%SS")
        ServerState.log.append(f"{time}: Update - {counter}")
        logging.info(f"Thread BusineesLogic: Updated Log - counter: {counter}")
        sleep(1)


@app.callback(Output("log1", "log"), Input("log1", "trigServLogUpdate"))
def startUpdate(trig : bool):
    logging.info("Thread Main: Received Trigger, Updating Log")
    return ServerState.log

if __name__ == '__main__':
    businessThread = threading.Thread(target=business_logic)
    businessThread.start()
    app.run_server(debug=True)
