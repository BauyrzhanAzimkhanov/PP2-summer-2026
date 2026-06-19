charForShapeDrawing = '*'

def draw_rectangle(length, width, charForDraw = charForShapeDrawing):
    global charForShapeDrawing
    print("Global variable before change:",charForShapeDrawing)
    charForShapeDrawing = "^"
    for i in range(width):
        for j in range(length):
            print(charForDraw, sep="", end=" ")
        print("\n", end="")

draw_rectangle(5, 3)

print()

draw_rectangle(6, 7, charForDraw="$")

print(charForShapeDrawing)


print("First", "Second", "Third", sep=", ")