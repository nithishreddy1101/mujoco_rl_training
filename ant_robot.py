import mujoco
import mujoco.viewer
import time

# 1. Load the model and data
model = mujoco.MjModel.from_xml_path('ant_robot.xml')
data = mujoco.MjData(model)

# 2. Launch the passive viewer
with mujoco.viewer.launch_passive(model, data) as viewer:
    # Optional: Set camera or visualization options
    viewer.cam.distance = 3.0
    
    while viewer.is_running():
        step_start = time.time()

        # 3. Advance the simulation
        mujoco.mj_step(model, data)

        # 4. Sync the viewer with the new data
        viewer.sync()

        # Rudimentary time-syncing to keep it real-time
        time_until_next_step = model.opt.timestep - (time.time() - step_start)
        if time_until_next_step > 0:
            time.sleep(time_until_next_step)
