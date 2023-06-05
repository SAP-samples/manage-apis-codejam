# tech-byte-diagram.py
from diagrams import Cluster, Diagram, Edge
from diagrams.custom import Custom
from diagrams.generic.device import Mobile
from diagrams.onprem.compute import Server
from diagrams.sap.integration import ProcessIntegration_Circle, APIManagement_Circle
from diagrams.sap.erp import SAPS4HANACloud
from diagrams.sap.saas import SAPSuccessfactorsBlack

# SAP BTP Solution Diagrams and Icons guidelines colors
L0_BLUE_COLOUR = "#316CCA"
L1_BLUE_COLOUR = "#074D92"
L2_GREEN_COLOUR = "#0F828F"
FIX_GREY_COLOUR = "#7F7F7F"
NON_SAP_AREA_COLOUR = "#595959"

GLOBALACCOUNT_GRAPH_ATTR = {"bgcolor": "white",
                            "pencolor": L0_BLUE_COLOUR, "penwidth":"3.0", "fontname": "72 Bold"}
SUBACCOUNT_GRAPH_ATTR = {"bgcolor": "white",
                         "pencolor": L1_BLUE_COLOUR, "penwidth":"2.5", "fontname": "72 Bold Italic"}
PRIMARY_EMPHASIZE_AREA_GRAPH_ATTR = {
    "bgcolor": "white", "pencolor": L2_GREEN_COLOUR, "penwidth":"2.0", "style": "dashed", "fontname": "72 Italic", "rankdir": "TB"}
SERVICES_GRAPH_ATTR = {"bgcolor": "white",
                            "pencolor": NON_SAP_AREA_COLOUR, "penwidth":"1.0", "fontname": "72 Bold"}

NODE_LABEL = {"fontname": "72 Regular"}
EDGE_LABEL = {"color": FIX_GREY_COLOUR, "fontname": "72 Italic"}

OPTIONAL_EDGE_LABEL = {"style": "dashed", "color": FIX_GREY_COLOUR, "fontname": "72 Italic"}

with Diagram("", show=False, filename="without-apim-data-flow", graph_attr={"splines": "false"}):
    mobile = Mobile("ITeLO end user", **NODE_LABEL)
    server = Server("ITeLO servers", **NODE_LABEL)

    with Cluster("Services", graph_attr=SERVICES_GRAPH_ATTR):
        nager_date = Custom("Nager.Date", "../nager-date.png")
        sap_server = SAPS4HANACloud(**{"height": "2.5", "width": "2.5"})
        ssff = SAPSuccessfactorsBlack(**{"height": "2.5", "width": "2.5"})
        cloud_integration = ProcessIntegration_Circle("Cloud Integration", **NODE_LABEL)

    mobile >> Edge(label="Business Partner API", **EDGE_LABEL) >> sap_server
    server >> Edge(label="Business Partner API", **EDGE_LABEL) >> sap_server

    mobile >> Edge(label="Employee Information API", **EDGE_LABEL) >> ssff
    server >> Edge(label="Employee Information API", **EDGE_LABEL) >> ssff
    
    mobile >> Edge(label="Public Holidays API", **EDGE_LABEL) >> nager_date
    server >> Edge(label="Public Holidays API", **EDGE_LABEL) >> nager_date

    with Cluster("SAP Business Technology Platform - Participant account", graph_attr=GLOBALACCOUNT_GRAPH_ATTR):
        with Cluster("Your Subaccount", graph_attr=SUBACCOUNT_GRAPH_ATTR):
            with Cluster("SAP Integration Suite", graph_attr=PRIMARY_EMPHASIZE_AREA_GRAPH_ATTR):
                server >> Edge(label="Integration Flow", **OPTIONAL_EDGE_LABEL) >> cloud_integration



                
