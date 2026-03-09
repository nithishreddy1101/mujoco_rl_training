import mujoco
import mujoco.viewer
import time

# Load the model
model = mujoco.MjModel.from_xml_path('line_follower.xml') # Replace with your filename
data = mujoco.MjData(model)

# Launch the passive viewer
with mujoco.viewer.launch_passive(model, data) as viewer:
    # Set a target velocity (radians per second)
    # 5.0 rad/s is roughly 48 RPM
    data.ctrl[0] = 10.0  # Left_Velocity
    data.ctrl[1] = 10.0  # Right_Velocity

    while viewer.is_running():
        step_start = time.time()

        # Step the simulation
        mujoco.mj_step(model, data)

        # Periodically sync the viewer
        viewer.sync()

        # Maintain real-time execution
        time_until_next_step = model.opt.timestep - (time.time() - step_start)
        if time_until_next_step > 0:
            time.sleep(time_until_next_step)