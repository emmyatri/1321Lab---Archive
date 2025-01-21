#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Assignment1A

print("[HTML Alert Generator]")
alert_message = input("Enter the alert message: ")  #user input for alert message

html_alert = '<div class=”g-alert”><p>' + alert_message + '</p></div>'
print("\nThis is the custom HTML Alert: \n" + html_alert)