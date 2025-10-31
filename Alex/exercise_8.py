'''
Exercise 8: Widgets and Gizmos
(15 Lines)
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order.
'''

print("Exercise Number 8")
number_of_widgets : int = int(input("Enter the number of widgets : "))
number_of_gizmos : int = int(input("Enter the number of gizmos : "))
widget_weight_grams : int = 75
gizmos_weight_grams : int = 112
total_weight_gizmos :int = number_of_gizmos * gizmos_weight_grams
total_weight_widgets : int = number_of_widgets * widget_weight_grams
total_of_order = total_weight_gizmos + total_weight_widgets
print(f"Total weight of widgets : {total_weight_widgets}. Total weight of gizmos : {total_weight_gizmos}")
print(f"Total weight of the order : {total_of_order}")