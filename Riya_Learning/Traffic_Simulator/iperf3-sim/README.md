python3.10+ &

Run "python setup_virtual_env_and_libraries.py". It will create virtual environment(venv folder) for python and install all required packages from requirements.txt file.


Activate the virtual environment by executing ".\myenv\Scripts\activate"
PS C:\Dixon_Project\MyLearning\Riya_Learning\Traffic_Simulator\iperf3-sim>.\myenv\Scripts\activate
(myenv) PS C:\Dixon_Projects\MyLearning\Riya_Learning\Traffic_Simulator\iperf3-sim>

And Deactivate the virtual environment by executing "deactivate"
(myenv) PS C:\Dixon_Projects\MyLearning\Riya_Learning\Traffic_Simulator\iperf3-sim>deactivate                       PS C:\Dixon_Projects\MyLearning\Riya_Learning\Traffic_Simulator\iperf3-sim>

Run the dixon_wifi_traffic_automation.py file to collect the traffic losses based on Bitrate, Packet Length and Timing Variation.
(myenv) PS C:\Dixon_Projects\MyLearning\Riya_Learning\Traffic_Simulator\iperf3-sim> python .\Dixon_Wifi_Traffic_Automation.py

Once log is collected in Logs folder, Run the below command to extract the loss percentage information and generate the graph in excel-sheet
(myenv) PS C:\Dixon_Projects\MyLearning\Riya_Learning\Traffic_Simulator\iperf3-sim> python .\Dixon_Log_Extracter_Graph_Generator.py