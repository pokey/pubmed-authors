from bs4 import BeautifulSoup
import grequests

headers = {
    'Pragma': 'no-cache',
    'Origin': 'https://www.ncbi.nlm.nih.gov',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'no-cache',
    'Referer': 'https://www.ncbi.nlm.nih.gov/pubmed/?term=tissue+cryopreservation',
    'Cookie': '_gat=1; _ga=GA1.2.1418271524.1478539062; WebEnv=1nu6Z5fw7nh0styREIF-yd-mednYiRsayQ0H94dZ2Eno5JE9CJ8lTXfZVHb8VVBAJoUl59VwbDnAD3uRbVJA8mGYWWxu7uVmLl7AM%40CE90DEF28284A291_0105SID; ncbi_sid=CE90DEF28284A291_0105SID; clicknext=link_id%3DDisplay%26link_name%3DDisplay%26link_href%3Dhttps%253A%252F%252Fwww.ncbi.nlm.nih.gov%252Fpubmed%252F%253Fterm%253Dtissue%252Bcryopreservation%2523%26link_text%3DFormat%253A%2520Summary%26link_class%3Djig-ncbipopper%26browserwidth%3D1097%26browserheight%3D86%26evt_coor_x%3D297%26evt_coor_y%3D118%26jseventms%3Do0lb8%26iscontextmenu%3Dfalse%26eventid%3D1%26jsevent%3Dclicknext%26ancestorId%3Dresult_action_bar%2Cmaincontent%26ancestorClassName%3Dinline_list%2Cleft%2Cdisplay_settings%2Cresults_settings%2Ctwo_settings%2Ccontent%2Ccol%2Cseven_col%26maxScroll_x%3D0%26maxScroll_y%3D325.7142857142857%26currScroll_x%3D0%26currScroll_y%3D96%26hasScrolled%3Dtrue%26ncbi_timeonpage%3D31268%26ncbi_onloadTime%3D26686%26ncbi_phid%3DCE8C1D6E828489910000000000F9006E%26sgSource%3Dnative; entrezSort=pubmed:; ncbi_prevPHID=CE8C1D6E828489910000000000F9006E; prevselfurl=https%3A//www.ncbi.nlm.nih.gov/pubmed/%3Fterm%3Dtissue+cryopreservation; unloadnext=jsevent%3Dunloadnext%26ncbi_pingaction%3Dunload%26ncbi_timeonpage%3D33999%26ncbi_onloadTime%3D26686%26eventid%3D2%26jsperf_dns%3D0%26jsperf_connect%3D820%26jsperf_ttfb%3D560%26jsperf_basePage%3D3868%26jsperf_frontEnd%3D26838%26jsperf_navType%3D2%26jsperf_redirectCount%3D0%26maxScroll_x%3D0%26maxScroll_y%3D325.7142857142857%26currScroll_x%3D0%26currScroll_y%3D96%26hasScrolled%3Dtrue%26ncbi_phid%3DCE8C1D6E828489910000000000F9006E%26sgSource%3Dnative',
    'Connection': 'keep-alive'
}

# This is the maximum page size
page_size = 100

data = {
    'term': 'tissue+cryopreservation+',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_PageController.PreviousPageName': 'results',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_PageController.SpecialPageName': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_Facets.FacetsUrlFrag': 'filters%3D',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_Facets.FacetSubmitted': 'false',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_Facets.BMFacets': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.sPresentation': 'xml',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.sSort': 'none',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.FFormat': 'docsum',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.FSort': '',
    'email_format': 'docsum',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.email_sort': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.email_count': str(page_size),
    'email_address': '',
    'email_subj': 'tissue+cryopreservation+-+PubMed',
    'email_add_text': '',
    'EmailCheck1': '',
    'EmailCheck2': '',
    'citman_count': str(page_size),
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.FileFormat': 'docsum',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.LastPresentation': 'docsum',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.Presentation': 'xml',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.PageSize': str(page_size),
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.LastPageSize': str(page_size),
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.Sort': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.LastSort': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.FileSort': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.Format': 'text',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.LastFormat': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.PrevPageSize': str(page_size),
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.PrevPresentation': 'docsum',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.PrevSort': '',
    'CollectionStartIndex': '1',
    'CitationManagerStartIndex': '1',
    'CitationManagerCustomRange': 'false',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_ResultsController.ResultCount': '10288',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_ResultsController.RunLastQuery': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.sPageSize': str(page_size),
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.EmailTab.EmailReport': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.EmailTab.EmailFormat': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.EmailTab.EmailCount': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.EmailTab.EmailStart': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.EmailTab.EmailSort': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.EmailTab.Email': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.EmailTab.EmailSubject': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.EmailTab.EmailText': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.EmailTab.EmailQueryKey': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.EmailTab.EmailHID': '1vyhJMUAaOTA5eDTLQSUWXyRddsYvejcbdi_axmx-mq1hl6Nyr_CP8vkxpjvGMGY1SD10QKlCHX9kfcGyd8Bg6kmbeZNMKSMQb',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.EmailTab.QueryDescription': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.EmailTab.Key': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.EmailTab.Answer': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.EmailTab.Holding': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.EmailTab.HoldingFft': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.EmailTab.HoldingNdiSet': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.EmailTab.OToolValue': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.EmailTab.SubjectList': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.TimelineAdPlaceHolder.CurrTimelineYear': '',
    'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.TimelineAdPlaceHolder.BlobID': 'NCID_1_8027235_130.14.22.215_9001_1479035434_1436486768_0MetA0_S_MegaStore_F_1',
    'EntrezSystem2.PEntrez.DbConnector.Db': 'pubmed',
    'EntrezSystem2.PEntrez.DbConnector.LastDb': 'pubmed',
    'EntrezSystem2.PEntrez.DbConnector.Term': 'tissue+cryopreservation',
    'EntrezSystem2.PEntrez.DbConnector.LastTabCmd': '',
    'EntrezSystem2.PEntrez.DbConnector.LastQueryKey': '1',
    'EntrezSystem2.PEntrez.DbConnector.IdsFromResult': '',
    'EntrezSystem2.PEntrez.DbConnector.LastIdsFromResult': '',
    'EntrezSystem2.PEntrez.DbConnector.LinkName': '',
    'EntrezSystem2.PEntrez.DbConnector.LinkReadableName': '',
    'EntrezSystem2.PEntrez.DbConnector.LinkSrcDb': '',
    'EntrezSystem2.PEntrez.DbConnector.Cmd': 'displaychanged',
    'EntrezSystem2.PEntrez.DbConnector.TabCmd': '',
    'EntrezSystem2.PEntrez.DbConnector.QueryKey': '',
    'p%24a': 'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.sPresentation',
    'p%24l': 'EntrezSystem2',
    'p%24st': 'pubmed'
}

def curr_data(page):
    return {
        'email_start': str(page*page_size+1),
        'coll_start': str(page*page_size+1),
        'citman_start': str(page*page_size+1),
        'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Entrez_Pager.CurrPage': str(page+1),
        'EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Entrez_Pager.cPage': str(page+1),
    }

rs = (
    grequests.post('https://www.ncbi.nlm.nih.gov/pubmed',
        headers=headers,
        data={**data, **curr_data(page)}
    )
    for page in range(103)
)

for i, r in enumerate(grequests.map(rs, size=20)):
    data = r.text
    soup = BeautifulSoup(data, "lxml")
    with open('pages/{}.xml'.format(i), 'w') as f:
        f.write(soup.pre.text)
