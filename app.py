{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyNDTOTOZxhDdxUk+MgYKpFZ"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","source":["!pip install -q streamlit"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"0ZSKLfZDTu0_","executionInfo":{"status":"ok","timestamp":1669824892161,"user_tz":-330,"elapsed":8432,"user":{"displayName":"APARNA BEHERA","userId":"07945046686698263384"}},"outputId":"44d0e3ab-df95-4576-f69f-4ce43b34b2b8"},"execution_count":3,"outputs":[{"output_type":"stream","name":"stdout","text":["\u001b[K     |████████████████████████████████| 10.3 MB 28.6 MB/s \n","\u001b[K     |████████████████████████████████| 164 kB 69.6 MB/s \n","\u001b[K     |████████████████████████████████| 182 kB 68.7 MB/s \n","\u001b[K     |████████████████████████████████| 237 kB 75.8 MB/s \n","\u001b[K     |████████████████████████████████| 4.7 MB 46.1 MB/s \n","\u001b[K     |████████████████████████████████| 78 kB 9.0 MB/s \n","\u001b[K     |████████████████████████████████| 62 kB 1.4 MB/s \n","\u001b[K     |████████████████████████████████| 51 kB 6.4 MB/s \n","\u001b[?25h  Building wheel for validators (setup.py) ... \u001b[?25l\u001b[?25hdone\n"]}]},{"cell_type":"code","source":["import streamlit as st\n","import pandas as pd\n","import numpy as np"],"metadata":{"id":"5WhHoINjRD-f","executionInfo":{"status":"ok","timestamp":1669824907102,"user_tz":-330,"elapsed":1122,"user":{"displayName":"APARNA BEHERA","userId":"07945046686698263384"}}},"execution_count":4,"outputs":[]},{"cell_type":"code","source":["def main():\n","  st.title(\"Find whether the given number is odd or even\")\n","  html_temp = \"\"\"\n","  <div style=\"background-color:black;padding:10px\">\n","  <h2 style=\"color:black;text-align:center;\">Division of 2 Numbers</h2>\n","  </div>\n","  \"\"\"\n","  st.markdown(html_temp,unsafe_allow_html=True)\n","  num = st.number_input(\"Number\")\n","  \n","  if(num % 2 == 0):\n","    result = 'even'\n","  else:\n","    result= 'odd'\n","  \n","  st.success('The number is {}'.format(result))\n","  \n","if __name__=='__main__':\n","  main()"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"Gv7WPrVbREG5","executionInfo":{"status":"ok","timestamp":1669824911323,"user_tz":-330,"elapsed":396,"user":{"displayName":"APARNA BEHERA","userId":"07945046686698263384"}},"outputId":"e4c4d2dd-f327-4fe5-8db1-2139a56f5538"},"execution_count":5,"outputs":[{"output_type":"stream","name":"stderr","text":["WARNING:root:\n","  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n","  command:\n","\n","    streamlit run /usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py [ARGUMENTS]\n","2022-11-30 16:15:11.816 \n","  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n","  command:\n","\n","    streamlit run /usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py [ARGUMENTS]\n"]}]},{"cell_type":"code","source":[],"metadata":{"id":"XZyZF5rFREKi"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":[],"metadata":{"id":"YIHb0pJgREOh"},"execution_count":null,"outputs":[]}]}