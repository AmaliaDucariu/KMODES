import matplotlib.pyplot as plt

cluster_no = [3, 4, 5, 6]
time_jobs = [17.957835, 18.134690, 19.529308, 20.863751]
# time_food_all_attr = [2.609793, 2.815772, 2.760939, 3.361768]
# time_food_main_ingr_sweet = [1.586537, 1.785508, 1.880045, 1.842473]
# time_food_main_ingr_sweet_fat = [1.985870, 2.152888, 1.485275, 2.042864]

plt.plot(cluster_no, time_jobs, color='g', label='Jobs')
# plt.plot(cluster_no, time_food_all_attr, color='c', label='ingredient principal + îndulcitor + grăsimi + condimente + alergeni')
# plt.plot(cluster_no, time_food_main_ingr_sweet, color='m', label='ingredient principal + îndulcitor')
# plt.plot(cluster_no, time_food_main_ingr_sweet_fat, color='y', label='ingredient principal + îndulcitor + grăsimi')

plt.xlabel("Număr de clustere")
plt.ylabel("Timpi de Execuție (s)")

plt.legend()
plt.show()