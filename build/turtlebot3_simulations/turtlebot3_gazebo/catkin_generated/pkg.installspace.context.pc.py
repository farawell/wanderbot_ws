# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include;/usr/include;/usr/include/gazebo-11;/usr/include/bullet;/usr/include/simbody;/usr/include/sdformat-9.10;/usr/include/ignition/math6;/usr/include/OGRE;/usr/include/OGRE/Terrain;/usr/include/OGRE/Paging;/usr/include/ignition/transport8;/usr/include/ignition/msgs5;/usr/include/ignition/common3;/usr/include/ignition/fuel_tools4".split(';') if "${prefix}/include;/usr/include;/usr/include/gazebo-11;/usr/include/bullet;/usr/include/simbody;/usr/include/sdformat-9.10;/usr/include/ignition/math6;/usr/include/OGRE;/usr/include/OGRE/Terrain;/usr/include/OGRE/Paging;/usr/include/ignition/transport8;/usr/include/ignition/msgs5;/usr/include/ignition/common3;/usr/include/ignition/fuel_tools4" != "" else []
PROJECT_CATKIN_DEPENDS = "roscpp;std_msgs;sensor_msgs;geometry_msgs;nav_msgs;tf;gazebo_ros".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lBulletSoftBody;-lBulletDynamics;-lBulletCollision;-lLinearMath;/usr/lib/x86_64-linux-gnu/libSimTKcommon.so.3.6;/usr/lib/x86_64-linux-gnu/libSimTKmath.so.3.6;/usr/lib/x86_64-linux-gnu/libSimTKsimbody.so.3.6;/usr/lib/x86_64-linux-gnu/libdart.so.6.9.2;/usr/lib/x86_64-linux-gnu/libgazebo.so;/usr/lib/x86_64-linux-gnu/libgazebo_client.so;/usr/lib/x86_64-linux-gnu/libgazebo_gui.so;/usr/lib/x86_64-linux-gnu/libgazebo_sensors.so;/usr/lib/x86_64-linux-gnu/libgazebo_rendering.so;/usr/lib/x86_64-linux-gnu/libgazebo_physics.so;/usr/lib/x86_64-linux-gnu/libgazebo_ode.so;/usr/lib/x86_64-linux-gnu/libgazebo_transport.so;/usr/lib/x86_64-linux-gnu/libgazebo_msgs.so;/usr/lib/x86_64-linux-gnu/libgazebo_util.so;/usr/lib/x86_64-linux-gnu/libgazebo_common.so;/usr/lib/x86_64-linux-gnu/libgazebo_gimpact.so;/usr/lib/x86_64-linux-gnu/libgazebo_opcode.so;/usr/lib/x86_64-linux-gnu/libgazebo_opende_ou.so;/usr/lib/x86_64-linux-gnu/libboost_system.so.1.71.0;/usr/lib/x86_64-linux-gnu/libboost_filesystem.so.1.71.0;/usr/lib/x86_64-linux-gnu/libboost_program_options.so.1.71.0;/usr/lib/x86_64-linux-gnu/libboost_regex.so.1.71.0;/usr/lib/x86_64-linux-gnu/libboost_iostreams.so.1.71.0;/usr/lib/x86_64-linux-gnu/libprotobuf.so;-lpthread;/usr/lib/x86_64-linux-gnu/libsdformat9.so.9.10.1;/usr/lib/x86_64-linux-gnu/libOgreMain.so;/usr/lib/x86_64-linux-gnu/libboost_thread.so.1.71.0;/usr/lib/x86_64-linux-gnu/libboost_date_time.so.1.71.0;/usr/lib/x86_64-linux-gnu/libOgreTerrain.so;/usr/lib/x86_64-linux-gnu/libOgrePaging.so;/usr/lib/x86_64-linux-gnu/libignition-math6.so.6.15.1;/usr/lib/x86_64-linux-gnu/libignition-transport8.so.8.5.0;/usr/lib/x86_64-linux-gnu/libignition-msgs5.so.5.11.0;/usr/lib/x86_64-linux-gnu/libignition-common3-graphics.so.3.17.0;/usr/lib/x86_64-linux-gnu/libignition-fuel_tools4.so.4.9.1".split(';') if "-lBulletSoftBody;-lBulletDynamics;-lBulletCollision;-lLinearMath;/usr/lib/x86_64-linux-gnu/libSimTKcommon.so.3.6;/usr/lib/x86_64-linux-gnu/libSimTKmath.so.3.6;/usr/lib/x86_64-linux-gnu/libSimTKsimbody.so.3.6;/usr/lib/x86_64-linux-gnu/libdart.so.6.9.2;/usr/lib/x86_64-linux-gnu/libgazebo.so;/usr/lib/x86_64-linux-gnu/libgazebo_client.so;/usr/lib/x86_64-linux-gnu/libgazebo_gui.so;/usr/lib/x86_64-linux-gnu/libgazebo_sensors.so;/usr/lib/x86_64-linux-gnu/libgazebo_rendering.so;/usr/lib/x86_64-linux-gnu/libgazebo_physics.so;/usr/lib/x86_64-linux-gnu/libgazebo_ode.so;/usr/lib/x86_64-linux-gnu/libgazebo_transport.so;/usr/lib/x86_64-linux-gnu/libgazebo_msgs.so;/usr/lib/x86_64-linux-gnu/libgazebo_util.so;/usr/lib/x86_64-linux-gnu/libgazebo_common.so;/usr/lib/x86_64-linux-gnu/libgazebo_gimpact.so;/usr/lib/x86_64-linux-gnu/libgazebo_opcode.so;/usr/lib/x86_64-linux-gnu/libgazebo_opende_ou.so;/usr/lib/x86_64-linux-gnu/libboost_system.so.1.71.0;/usr/lib/x86_64-linux-gnu/libboost_filesystem.so.1.71.0;/usr/lib/x86_64-linux-gnu/libboost_program_options.so.1.71.0;/usr/lib/x86_64-linux-gnu/libboost_regex.so.1.71.0;/usr/lib/x86_64-linux-gnu/libboost_iostreams.so.1.71.0;/usr/lib/x86_64-linux-gnu/libprotobuf.so;-lpthread;/usr/lib/x86_64-linux-gnu/libsdformat9.so.9.10.1;/usr/lib/x86_64-linux-gnu/libOgreMain.so;/usr/lib/x86_64-linux-gnu/libboost_thread.so.1.71.0;/usr/lib/x86_64-linux-gnu/libboost_date_time.so.1.71.0;/usr/lib/x86_64-linux-gnu/libOgreTerrain.so;/usr/lib/x86_64-linux-gnu/libOgrePaging.so;/usr/lib/x86_64-linux-gnu/libignition-math6.so.6.15.1;/usr/lib/x86_64-linux-gnu/libignition-transport8.so.8.5.0;/usr/lib/x86_64-linux-gnu/libignition-msgs5.so.5.11.0;/usr/lib/x86_64-linux-gnu/libignition-common3-graphics.so.3.17.0;/usr/lib/x86_64-linux-gnu/libignition-fuel_tools4.so.4.9.1" != "" else []
PROJECT_NAME = "turtlebot3_gazebo"
PROJECT_SPACE_DIR = "/home/rirolab/wanderbot_ws/install"
PROJECT_VERSION = "1.3.2"
