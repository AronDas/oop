class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


modelLx = vehicle(200, 500)


print("ModelLx max speed is:",modelLx.max_speed)
print("ModelLx max mileage is:",modelLx.mileage)
