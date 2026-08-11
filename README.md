# ros2-turtlesim-square-motion 
A simple **ROS 2 Python node** that controls the `turtlesim` turtle to move in a square-shaped path using velocity commands.

---

##  Overview

The `TurtleSquare` node publishes `Twist` messages to the `/turtle1/cmd_vel` topic.

The node uses a simple state machine triggered by a timer:

* **State 0 – Move Forward:** The turtle moves forward with a linear velocity of `2.0 m/s`.
* **State 1 – Rotate 90°:** The turtle stops moving forward and rotates with an angular velocity of `π/2 rad/s`.

The two states alternate continuously to create a square movement pattern.

---

## Features

* **Precise Square Trajectory:** Alternates between moving forward and making accurate 90-degree ($\frac{\pi}{2}$) turns.
* **ROS 2 Native:** Built using `rclpy` and standard `geometry_msgs/msg/Twist` messages.
* **Informative Logging:** Prints real-time status updates to the terminal during each phase of movement.

---

## Requirements

Before running the node, make sure you have:

* Ubuntu
* ROS 2
* Python 3
* `turtlesim` package

---

## How to Run

### 1. Start turtlesim

Open a terminal and source your ROS 2 environment:

```bash
source /opt/ros/<ros2_distro>/setup.bash
```

Then start `turtlesim`:

```bash
ros2 run turtlesim turtlesim_node
```

Replace `<ros2_distro>` with your installed ROS 2 distribution, such as `humble`, `jazzy`, or another supported version.

### 2. Run the Publisher Node

Open a **second terminal** and source the ROS 2 environment:

```bash
source /opt/ros/<ros2_distro>/setup.bash
```

Then execute the Python script:

```bash
python3 turtle_square.py
```

---

## Code 

The main node is implemented using `rclpy` and publishes `Twist` messages to the turtle's velocity command topic.

```python
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class TurtleSquarePublisher(Node):
    def __init__(self):
        super().__init__('turtle_square_publisher')
        self.publisher_ = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )
        self.timer = self.create_timer(1.0, self.move_in_square)
        self.state = 0

    def move_in_square(self):
        msg = Twist()

        if self.state == 0:
            msg.linear.x = 2.0
            msg.angular.z = 0.0
            self.get_logger().info(
                'Executing forward movement along square path'
            )
            self.state = 1

        else:
            msg.linear.x = 0.0
            msg.angular.z = math.pi / 2.0
            self.get_logger().info(
                'Executing 90-degree turn for square corner'
            )
            self.state = 0

        self.publisher_.publish(msg)
```

## How It Works

The timer calls `move_in_square()` every **1 second**.

The state alternates between:

| State | Linear Velocity | Angular Velocity | Action       |
| ----- | --------------: | ---------------: | ------------ |
| `0`   |           `2.0` |            `0.0` | Move forward |
| `1`   |           `0.0` |            `π/2` | Rotate       |

The node continuously switches between these two states and publishes the corresponding velocity command.

## Expected Result

When the node is running together with `turtlesim`, the turtle receives alternating forward and rotational velocity commands, producing a repeating square-like movement pattern.

<img width="545" height="512" alt="Screenshot 2026-08-11 114200" src="https://github.com/user-attachments/assets/e71ba6c6-1789-45a9-9790-d82bd89bd884" />

## Important Note

This implementation demonstrates the **state-machine concept**, but using a fixed 1-second timer does not precisely guarantee that the turtle will draw a perfect square.

For a more accurate square, the node should keep track of the elapsed time or distance for each side and rotation angle, then stop each movement at the correct point.

[see motion]()
