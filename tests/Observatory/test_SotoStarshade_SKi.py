from EXOSIMS.Observatory.SotoStarshade_SKi import SotoStarshade_SKi as sss
import unittest
import numpy as np
import astropy.units as u
from scipy.integrate import solve_ivp
import astropy.constants as const
import hashlib
import scipy.optimize as optimize
from scipy.optimize import basinhopping
import scipy.interpolate as interp
import scipy.integrate as intg
from scipy.integrate import solve_bvp
from copy import deepcopy
import time
import os
import pickle

class TestSotoStarshadeSKi(unittest.TestCase):
    """
    Sonny Rappaport, July 2021, Cornell

    This class tests particular methods from SotoStarshade_Ski. 
    
    """

    def test_convertTime_to_dim(self):
      
        """tests covertTime_to_dim with some trivial inputs, with outputs generated
        via a locally run Jupyter notebook with python """


        #tests an array of input integers from 0 to 100

        input = np.linspace(0, 100, num=101)
        output = u.yr*[0.0, 0.15915494309189535, 0.3183098861837907, 0.477464829275686, 0.6366197723675814, 0.7957747154594768, 0.954929658551372, 1.1140846016432675, 1.2732395447351628, 1.432394487827058, 1.5915494309189535, 1.7507043740108488, 1.909859317102744, 2.0690142601946393, 2.228169203286535, 2.3873241463784303, 2.5464790894703255, 2.705634032562221, 2.864788975654116, 3.0239439187460113, 3.183098861837907, 3.3422538049298023, 3.5014087480216975, 3.660563691113593, 3.819718634205488, 3.9788735772973833, 4.138028520389279, 4.297183463481174, 4.45633840657307, 4.615493349664965, 4.7746482927568605, 4.933803235848756, 5.092958178940651, 5.252113122032546, 5.411268065124442, 5.570423008216337, 5.729577951308232, 5.888732894400127, 6.047887837492023, 6.207042780583918, 6.366197723675814, 6.525352666767709, 6.684507609859605, 6.8436625529515, 7.002817496043395, 7.16197243913529, 7.321127382227186, 7.480282325319081, 7.639437268410976, 7.798592211502871, 7.957747154594767, 8.116902097686662, 8.276057040778557, 8.435211983870452, 8.594366926962348, 8.753521870054243, 8.91267681314614, 9.071831756238035, 9.23098669932993, 9.390141642421826, 9.549296585513721, 9.708451528605616, 9.867606471697512, 10.026761414789407, 10.185916357881302, 10.345071300973197, 10.504226244065093, 10.663381187156988, 10.822536130248883, 10.981691073340778, 11.140846016432674, 11.300000959524569, 11.459155902616464, 11.61831084570836, 11.777465788800255, 11.93662073189215, 12.095775674984045, 12.25493061807594, 12.414085561167836, 12.573240504259733, 12.732395447351628, 12.891550390443523, 13.050705333535419, 13.209860276627314, 13.36901521971921, 13.528170162811104, 13.687325105903, 13.846480048994895, 14.00563499208679, 14.164789935178685, 14.32394487827058, 14.483099821362476, 14.642254764454371, 14.801409707546267, 14.960564650638162, 15.119719593730057, 15.278874536821952, 15.438029479913848, 15.597184423005743, 15.756339366097638, 15.915494309189533]

        np.testing.assert_array_equal(sss.convertTime_to_dim(self,input),output)

    def test_convertPos_to_dim(self):

      """tests convertPos_to_dim with some trivial inputs. Because the canonical 
      units are in AU, simply check to see that the input is returned with astropy
      AU units attached. 
      """

      input = np.linspace(0,100, num=101)
      np.testing.assert_array_equal(sss.convertPos_to_dim(self,input),input*u.AU)