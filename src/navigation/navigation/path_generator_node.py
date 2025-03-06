import rclpy  #pour ecrire des noeuds dans python
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped 
from nav_msgs.msg import Path 
from navigation.srv import PlanPath #importer le service PlanPath


class PathGeneratorNode(Node):
    #constructeur :
    def __init__(self, node_name ="path_generator_node", *, context = None, cli_args = None, namespace = None, use_global_arguments = True, enable_rosout = True, start_parameter_services = True, parameter_overrides = None, allow_undeclared_parameters = False, automatically_declare_parameters_from_overrides = False):
        super().__init__(node_name)
        #Creation d'un éditeur  publisher 
        self.publisher_=self.create_publisher(PoseStamped,'Generator_path',10)
        self.destination =None

        #Creation d'un service pour le choix de la destination 
        self.service = self.create_service(PlanPath,'set_destination',self.path_generetor_callback)

        #Creation d'un timer pour la publication du chemin si une destination est definie:
        self.timer = self.create_timer(1.0,self.path_generator_callback)
        self.get_logger().info('Path Generator node started...')


    #Function of destination callback:


    def path_generetor_callback(self,request,response):

         # Verfier si la requete contient des coordonnees valides ;
        try: 
            #s'assurer que les coordonnes sont des nombres:
            x= float(PlanPath.request.x)
            y= float(PlanPath.request.y)
            self.destination = (x,y)
            self.get_logger().info(f'Destination set to : {self.destination}')
            response.success =True
            response.messsage ="Destination defined successfully ✨"
            #retourner la reponse:
            if self.destination:

            #La generation du chemin vers la destination:

                path = Path()
                path.header.frame_id = "map"
                path.header.stamp = self.get_clock().now().to_msg()
                steps = 50
            #Generer le chemin en fonction du nombre d'etapes:
                for i in range(steps+1):
                    pose =PoseStamped()
                    pose.header.frame_id = "map"
                    pose.pose.position.x= i* self.destination[0]/steps
                    pose.pose.position.y= i* self.destination[1]/steps
                    pose.pose.orientation.w =1.0
                    path.poses.append(pose)

            self.publisher_.publish(path)
            self.get_logger().info(f'Path generated and published... {i}/{steps}')
            
            self.timer.cancel()
            response.success = True
            response.messsage ="Path generated successfully ✨"
            return response
        
        except ValueError:

            self.get_logger().error("Invalid destination ❌: x and y must be numbers.")
            response.success = False
            response.messsage ="Error‼️ : x and y must be valid numbers."
            return response
        


            
#Fonction principal:
def main ():
    #Initialize ROS communications for a given context.
    rclpy.init() 
    # Creerune instance de la classe PathGeneratedNode  
    node = PathGeneratorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down Path Generator Node.")
    finally:
        node.destroy_node()
        rclpy.shutdown()


#Point d'entree:
if __name__ == '__main__':
    main()


