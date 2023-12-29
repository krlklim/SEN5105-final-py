# Solutions for the final exam for SEN5105
### Bahcesehir University | Master degree
All solutions can be found in the ***[src](https://github.com/krlklim/SEN5105-final-py/tree/main/src)*** directory

### Question 1. CAESAR CIPHER ###
Simple solution to encrypt and decrypt any text using caesar 
cipher. In this solution I used **subprocess** python library
to give an ability for the user to auto-copy encrypted and
decrypt message after it was generated.

Example usage in the code:
```python
subprocess.run("pbcopy", text=True, input=res_msg)
```
Solution can be run in the shell console with the following
command:
```bash
python q1_caesar_sipher/caesarcipher.py
# or
python3 q1_caesar_sipher/caesarcipher.py
```

### Question 2. TRIVIA GAME ###
Questions were parsed from [source questions
library](https://gist.github.com/khamer/66102c745a9a75de997c038e3166a95d) with a ruby script. In the program, we are taking
10 random questions from the first dictionary (which was 
fulfilled from the parsed JSON file with questions) and
then creating a dictionary with a 10 Question objects.

Solution can be run in the shell console with the following
command:
```bash
python q2_trivia_game/triviagame.py
# or
python3 q2_trivia_gametriviagame.py
```

### Question 3. PATIENT INFORMATION ###
In this solution I used two python libraries: **PrettyTable**
and **datetime**. **Datetime** is a standard Python library 
to get and display current date. **PrettyTable** is a python 
library to create and display tables in the console output.

**PrettyTable** library can be installed with:
```bash
pip install prettytable
# or
pip3 install prettytable
```
Solution can be run in the shell console with the following
command:
```bash
python q3_patient_information/main.py
# or
python3 q3_patient_information/main.py
```
