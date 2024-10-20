drop = float(input("Enter the Height from which the ball is dropped: "))
bounce = int(input("Enter the number of times the ball bounced: "))
totalDistance = drop
for i in range(bounce):
    drop*= 0.5
    totalDistance += 2 * drop
print("The total distance travelled by the ball was: ", totalDistance)
