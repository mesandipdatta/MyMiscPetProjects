# =================================================================================================
# Author - Sandip Datta
#
# This is a Dash-Pytohn application. 
#
# You can boot a Dash server through python script and generate\publish charts\graphs as
#     Intercative Web apps on default port 8050 (or any custom port)
# 
#
# How to run  - $ python main.py "scatter"
#		or		$ python main.py "bar"
#		or		$ python main.py "table"		
#
#==================================================================================================

import myapp
import sys

import dash
from dash.dependencies import Event, Output
import dash_html_components as html
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from pandas_datareader import data as web
from datetime import datetime as dt

#app = dash.Dash(__name__)
app = dash.Dash("DashWebApp")
app.config.supress_callback_exceptions = True

#=== Build the Graph apps
# Currently handled args - "scatter" , "bar", "table" 
graph_type = sys.argv[1]
myapp.dashapp(graph_type,app)

#=== Run the Graphs & Publish as web apps
print "===== Running the Server and Publish web-apps ===="
app.run_server(port=8050,debug=True)