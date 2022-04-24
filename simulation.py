from turtle import width
from manim import *
import coordinates
import coordinates2

class simu(Scene):
    def construct(self):
        def get_li(x1,y1,x2,y2,c):
            if c==0:
                linea=Line(start=[x1,y1,0],end=[x2,y2,0],color=DARK_BLUE).set_opacity(1)
                return linea
            else:
                linea=Line(start=[x1,y1,0],end=[x2,y2,0],color=RED_D).set_opacity(1)
                return linea

        
        def get_dot(x1,y1):
            dot1= Dot([x1,y1,0])
            return dot1
        

        
        track=ValueTracker(0)
        
        final_line1=always_redraw(lambda: get_li(0,2,coordinates.cordi[int(track.get_value())][0],coordinates.cordi[int(track.get_value())][1]+2,0))
        final_line2=always_redraw(lambda: get_li(coordinates.cordi[int(track.get_value())][0],coordinates.cordi[int(track.get_value())][1]+2,coordinates.cordi[int(track.get_value())][2],coordinates.cordi[int(track.get_value())][3]+2,1))
        # final_line3=always_redraw(lambda: get_li(0,2,coordinates2.cordi[int(track.get_value())][0],coordinates2.cordi[int(track.get_value())][1]+2,0))
        # final_line4=always_redraw(lambda: get_li(coordinates2.cordi[int(track.get_value())][0],coordinates2.cordi[int(track.get_value())][1]+2,coordinates2.cordi[int(track.get_value())][2],coordinates2.cordi[int(track.get_value())][3]+2,1))
        final_dot=always_redraw(lambda: get_dot(coordinates.cordi[int(track.get_value())][2],coordinates.cordi[int(track.get_value())][3]+2))
        # final_dot2=always_redraw(lambda: get_dot(coordinates2.cordi[int(track.get_value())][2],coordinates2.cordi[int(track.get_value())][3]+2))
       
        path=VMobject(stroke_color=PINK,stroke_opacity=0.7,stroke_width=1)
        def update_path(path):
            previous_path = path.copy()
            
            previous_path.add_points_as_corners([final_dot.get_center()])      
            path.become(previous_path)
            
        path.set_points_as_corners([final_dot.get_center(), final_dot.get_center()])
        
        path.add_updater(update_path)
        
       
        # path2=VMobject(stroke_color=YELLOW,stroke_opacity=0.7,stroke_width=1)
        # def update_path(path2):
        #     previous_path = path2.copy()
            
        #     previous_path.add_points_as_corners([final_dot2.get_center()])      
        #     path2.become(previous_path)
            
        # path2.set_points_as_corners([final_dot2.get_center(), final_dot2.get_center()])
        
        # path2.add_updater(update_path)
        
        self.add(final_line1,final_line2,final_dot,path)
        self.play(track.animate.set_value(19950),rate_func=linear,run_time=198)
        self.wait()