'''
Created on Jul 15, 2014

@author: rajni
'''
from bs4 import BeautifulSoup
import urllib
urls='''<html><a href="bankdetails.jsp?bank_id=12455">ADB ALAPPUZHA</a>
<a href="bankdetails.jsp?bank_id=12457">ADB CHANGANACHERRY</a>
<a href="bankdetails.jsp?bank_id=12459">ADB KAINATTY</a>
<a href="bankdetails.jsp?bank_id=12461">ADB KUNNAMKULAM</a>
<a href="bankdetails.jsp?bank_id=12463">ADB PAYYANNUR</a>
<a href="bankdetails.jsp?bank_id=12465">ADIMALY</a>
<a href="bankdetails.jsp?bank_id=12466">AGALI</a>
<a href="bankdetails.jsp?bank_id=12468">ALAKODE</a>
<a href="bankdetails.jsp?bank_id=12470">ALTHARA JUNCTION</a>
<a href="bankdetails.jsp?bank_id=12472">ALWAYE TOWN</a>
<a href="bankdetails.jsp?bank_id=128745">AMBALAPUZHA</a>
<a href="bankdetails.jsp?bank_id=12475">ANJUKUNNU</a>
<a href="bankdetails.jsp?bank_id=12476">AROOR</a>
<a href="bankdetails.jsp?bank_id=12478">ARTHINKAL</a>
<a href="bankdetails.jsp?bank_id=12480">ASOKAPURAM</a>
<a href="bankdetails.jsp?bank_id=12481">ATTINGAL</a>
<a href="bankdetails.jsp?bank_id=125410">AYARKUNNAM</a>
<a href="bankdetails.jsp?bank_id=125397">AZHIKODE</a>
<a href="bankdetails.jsp?bank_id=128378">BANERJI ROAD BRANCH ERNAK...</a>
<a href="bankdetails.jsp?bank_id=125491">BHARANIKAVU</a>
<a href="bankdetails.jsp?bank_id=12487">C E P Z COCHIN</a>
<a href="bankdetails.jsp?bank_id=12488">CALICUT</a>
<a href="bankdetails.jsp?bank_id=12490">CALICUT REG. ENGINEE</a>
<a href="bankdetails.jsp?bank_id=125501">CCPC THIRUVANANTHAPURAM</a>
<a href="bankdetails.jsp?bank_id=125514">CENTRALISED PENSION PROCE...</a>
<a href="bankdetails.jsp?bank_id=125504">CGO COMPLEX</a>
<a href="bankdetails.jsp?bank_id=12492">CHANGANACHERRY</a>
<a href="bankdetails.jsp?bank_id=154335">CHEEMENI</a>
<a href="bankdetails.jsp?bank_id=154680">CHELAKKARA</a>
<a href="bankdetails.jsp?bank_id=12496">CHERAI</a>
<a href="bankdetails.jsp?bank_id=12498">CHERIAPILLY</a>
<a href="bankdetails.jsp?bank_id=12499">CHERPU</a>
<a href="bankdetails.jsp?bank_id=125486">CHERTHALA SOUTH</a>
<a href="bankdetails.jsp?bank_id=125518">CHIRAYINKEEZHU</a>
<a href="bankdetails.jsp?bank_id=125458">CHOTTANIKARA</a>
<a href="bankdetails.jsp?bank_id=125415">CHUNDALE</a>
<a href="bankdetails.jsp?bank_id=125399">CIVIL STATION KASARAGOD</a>
<a href="bankdetails.jsp?bank_id=125500">CIVIL STATION THIRUVANANT...</a>
<a href="bankdetails.jsp?bank_id=125462">CO-OP. MEDICAL COLLEGE</a>
<a href="bankdetails.jsp?bank_id=12505">COCHIN PORT TRUST</a>
<a href="bankdetails.jsp?bank_id=12507">COMMERCIAL BR, ERNAK</a>
<a href="bankdetails.jsp?bank_id=125498">COMMERCIAL BRANCH THIRUVA...</a>
<a href="bankdetails.jsp?bank_id=125459">DE-PAUL ATHANI</a>
<a href="bankdetails.jsp?bank_id=12509">EAST FORT, TRICHUR</a>
<a href="bankdetails.jsp?bank_id=12511">EDAMUTTAM</a>
<a href="bankdetails.jsp?bank_id=125419">EDAPPAL</a>
<a href="bankdetails.jsp?bank_id=125121">EDAYAKURICHI </a>
<a href="bankdetails.jsp?bank_id=12513">ELAMANNUR</a>
<a href="bankdetails.jsp?bank_id=12515">ELATHUR</a>
<a href="bankdetails.jsp?bank_id=12517">ERNAKULAM</a>
<a href="bankdetails.jsp?bank_id=125473">ETTUMANOOR</a>
<a href="bankdetails.jsp?bank_id=125440">FACT ELOOR</a>
<a href="bankdetails.jsp?bank_id=125523">FUND SETTLEMENT LINK OFFI...</a>
<a href="bankdetails.jsp?bank_id=12519">GURUVAYUR</a>
<a href="bankdetails.jsp?bank_id=125452">HIGH COURT OF KERALA</a>
<a href="bankdetails.jsp?bank_id=125401">IIM KOZHIKODE</a>
<a href="bankdetails.jsp?bank_id=12520">IRINJALAKUDA</a>
<a href="bankdetails.jsp?bank_id=125433">KADAMPAZHIPURAM</a>
<a href="bankdetails.jsp?bank_id=12522">KADAPPURAM</a>
<a href="bankdetails.jsp?bank_id=125485">KAICHOONDI</a>
<a href="bankdetails.jsp?bank_id=12525">KAIPUZHA</a>
<a href="bankdetails.jsp?bank_id=125455">KALAMASSERRY SOUTH</a>
<a href="bankdetails.jsp?bank_id=154452">KALATHIPADY</a>
<a href="bankdetails.jsp?bank_id=12527">KALLAI ROAD</a>
<a href="bankdetails.jsp?bank_id=12528">KALOOR</a>
<a href="bankdetails.jsp?bank_id=12530">KANHANGAD</a>
<a href="bankdetails.jsp?bank_id=125471">KANJIRAMATTOM</a>
<a href="bankdetails.jsp?bank_id=12531">KANJIRAPUZHA</a>
<a href="bankdetails.jsp?bank_id=125496">KANNANALLUR</a>
<a href="bankdetails.jsp?bank_id=12534">KANNUR TOWN</a>
<a href="bankdetails.jsp?bank_id=12536">KARALAM</a>
<a href="bankdetails.jsp?bank_id=12537">KARAVALUR</a>
<a href="bankdetails.jsp?bank_id=12538">KASARGOD</a>
<a href="bankdetails.jsp?bank_id=12540">KATTOOR</a>
<a href="bankdetails.jsp?bank_id=125508">KAZHAKKOOTTAM</a>
<a href="bankdetails.jsp?bank_id=125436">KERALA POLICE ACADEMY THR...</a>
<a href="bankdetails.jsp?bank_id=12542">KERALASSERY</a>
<a href="bankdetails.jsp?bank_id=154681">KODAKARA</a>
<a href="bankdetails.jsp?bank_id=125480">KODIMATHA</a>
<a href="bankdetails.jsp?bank_id=12544">KODUVALLY</a>
<a href="bankdetails.jsp?bank_id=125483">KOLLAKKADAVU</a>
<a href="bankdetails.jsp?bank_id=12546">KOMMADY</a>
<a href="bankdetails.jsp?bank_id=140441">KONGAD</a>
<a href="bankdetails.jsp?bank_id=154579">KONNI</a>
<a href="bankdetails.jsp?bank_id=128540">KOOTTANAD</a>
<a href="bankdetails.jsp?bank_id=12550">KOTHAMANGALAM</a>
<a href="bankdetails.jsp?bank_id=12551">KOTTAMAM</a>
<a href="bankdetails.jsp?bank_id=12552">KOTTATHARA</a>
<a href="bankdetails.jsp?bank_id=125443">KOTTAYI</a>
<a href="bankdetails.jsp?bank_id=12555">KOZHENCHERRY</a>
<a href="bankdetails.jsp?bank_id=140272">KUMBALA</a>
<a href="bankdetails.jsp?bank_id=12556">KUMBANAD</a>
<a href="bankdetails.jsp?bank_id=125429">KUNNATHURMEDU</a>
<a href="bankdetails.jsp?bank_id=125479">KURAVILANGAD</a>
<a href="bankdetails.jsp?bank_id=12558">KURUMANNU</a>
<a href="bankdetails.jsp?bank_id=12559">KUTHUPARAMBA</a>
<a href="bankdetails.jsp?bank_id=12560">KUTTICHIRA</a>
<a href="bankdetails.jsp?bank_id=12562">M G ROAD ERNAKULAM</a>
<a href="bankdetails.jsp?bank_id=136197">MALA</a>
<a href="bankdetails.jsp?bank_id=12563">MALAPARAMBA</a>
<a href="bankdetails.jsp?bank_id=128633">MALLAPALLY</a>
<a href="bankdetails.jsp?bank_id=125413">MANANTHAVADY</a>
<a href="bankdetails.jsp?bank_id=12566">MANIMOOLY</a>
<a href="bankdetails.jsp?bank_id=125418">MANJERI MALLAPURAM</a>
<a href="bankdetails.jsp?bank_id=125476">MANNANAM</a>
<a href="bankdetails.jsp?bank_id=125425">MANNARKKAD</a>
<a href="bankdetails.jsp?bank_id=12569">MARAKKADA ROAD</a>
<a href="bankdetails.jsp?bank_id=12571">MARKET ROAD,THIRUVAL</a>
<a href="bankdetails.jsp?bank_id=12573">MAVELIKARA</a>
<a href="bankdetails.jsp?bank_id=125431">MEENAKSHIPURAM</a>
<a href="bankdetails.jsp?bank_id=125412">MEPPADI</a>
<a href="bankdetails.jsp?bank_id=125470">MINICOY</a>
<a href="bankdetails.jsp?bank_id=12576">MOOZHIKULAM</a>
<a href="bankdetails.jsp?bank_id=140148">MUKTANAND (KARELIBAUG)</a>
<a href="bankdetails.jsp?bank_id=12578">MULLAKKAL</a>
<a href="bankdetails.jsp?bank_id=125434">MUTHALAMADA</a>
<a href="bankdetails.jsp?bank_id=12581">MUTHUTHALA</a>
<a href="bankdetails.jsp?bank_id=12583">NADAKKAVU</a>
<a href="bankdetails.jsp?bank_id=12584">NANTHENCODE</a>
<a href="bankdetails.jsp?bank_id=12585">NAVAL ACADEMY EZHIMA</a>
<a href="bankdetails.jsp?bank_id=12586">NEDIASALA</a>
<a href="bankdetails.jsp?bank_id=128811">NEDUMBASSERY</a>
<a href="bankdetails.jsp?bank_id=125487">NELLAD</a>
<a href="bankdetails.jsp?bank_id=125466">NERIAMANGALAM</a>
<a href="bankdetails.jsp?bank_id=12588">NH 47 ALAPPUZHA</a>
<a href="bankdetails.jsp?bank_id=125461">NIRMALA COLLEGE</a>
<a href="bankdetails.jsp?bank_id=125454">NORTH PARUR</a>
<a href="bankdetails.jsp?bank_id=12591">NRI BRANCH ERNAKULAM</a>
<a href="bankdetails.jsp?bank_id=140270">NRI BRANCH, KANNUR</a>
<a href="bankdetails.jsp?bank_id=154682">NRI BRANCH, THRISSUR</a>
<a href="bankdetails.jsp?bank_id=125520">OAD ZO THIRUVANANTHAPURAM</a>
<a href="bankdetails.jsp?bank_id=125406">OMASSERI</a>
<a href="bankdetails.jsp?bank_id=12595">OTTAPALAM</a>
<a href="bankdetails.jsp?bank_id=154552">PADINJARANGADI</a>
<a href="bankdetails.jsp?bank_id=12597">PALAI</a>
<a href="bankdetails.jsp?bank_id=12599">PALAKKAD TOWN</a>
<a href="bankdetails.jsp?bank_id=12600">PALARIVATTOM</a>
<a href="bankdetails.jsp?bank_id=12601">PALAYAM,CALICUT</a>
<a href="bankdetails.jsp?bank_id=12603">PAMBANAR</a>
<a href="bankdetails.jsp?bank_id=136478">PAMPADY</a>
<a href="bankdetails.jsp?bank_id=136258">PANAVILA</a>
<a href="bankdetails.jsp?bank_id=12604">PANAYAPALLY</a>
<a href="bankdetails.jsp?bank_id=12605">PANJAL</a>
<a href="bankdetails.jsp?bank_id=125516">PARASSALA</a>
<a href="bankdetails.jsp?bank_id=12607">PATHANAMTHITTA</a>
<a href="bankdetails.jsp?bank_id=125424">PATTAMBI</a>
<a href="bankdetails.jsp?bank_id=12609">PAVANGAD</a>
<a href="bankdetails.jsp?bank_id=125403">PBB CALICUT</a>
<a href="bankdetails.jsp?bank_id=12611">PERINTHALMANNA</a>
<a href="bankdetails.jsp?bank_id=12613">PERSONAL BANKING BR,</a>
<a href="bankdetails.jsp?bank_id=12615">PERUMBAVOOR</a>
<a href="bankdetails.jsp?bank_id=128725">PETTA</a>
<a href="bankdetails.jsp?bank_id=12617">PONGANADU</a>
<a href="bankdetails.jsp?bank_id=12618">POONOOR</a>
<a href="bankdetails.jsp?bank_id=12619">POTHANICAD</a>
<a href="bankdetails.jsp?bank_id=12621">POYYA</a>
<a href="bankdetails.jsp?bank_id=136202">PUNNAKKAL</a>
<a href="bankdetails.jsp?bank_id=12623">PUNNAYUR</a>
<a href="bankdetails.jsp?bank_id=12625">PUTHUVIPE</a>
<a href="bankdetails.jsp?bank_id=136673">PUTHYITHERU</a>
<a href="bankdetails.jsp?bank_id=12627">QUILANDY</a>
<a href="bankdetails.jsp?bank_id=125515">RACPC THIRUVANANTHAPURAM</a>
<a href="bankdetails.jsp?bank_id=12629">RAMANKULANGARA</a>
<a href="bankdetails.jsp?bank_id=125834">RANI SARAI</a>
<a href="bankdetails.jsp?bank_id=125423">RASMECC PALAKKAD</a>
<a href="bankdetails.jsp?bank_id=125492">RASMECCC KOLLAM</a>
<a href="bankdetails.jsp?bank_id=140319">RBO II  DHARAMPUR</a>
<a href="bankdetails.jsp?bank_id=140060">RCPC CALICUT</a>
<a href="bankdetails.jsp?bank_id=140061">RCPC, KOTTAYAM</a>
<a href="bankdetails.jsp?bank_id=12631">S S I BR ERNAKULAM</a>
<a href="bankdetails.jsp?bank_id=125472">SAMARITAN HOSPITALPAZHANG...</a>
<a href="bankdetails.jsp?bank_id=125253">SATHUVACHARI</a>
<a href="bankdetails.jsp?bank_id=12633">SERVICE BRANCH TIRUV</a>
<a href="bankdetails.jsp?bank_id=12635">SIB KANNUR</a>
<a href="bankdetails.jsp?bank_id=12637">SIB TRISSUR</a>
<a href="bankdetails.jsp?bank_id=125464">SME CITY CREDIT CENTRE</a>
<a href="bankdetails.jsp?bank_id=140280">SOUTH CHITTOOR</a>
<a href="bankdetails.jsp?bank_id=125499">SPBB THIRUVANANTHAPURAM</a>
<a href="bankdetails.jsp?bank_id=154453">SPL.PBB KOTTAYAM</a>
<a href="bankdetails.jsp?bank_id=12641">SSI BRANCH KANJIKODE</a>
<a href="bankdetails.jsp?bank_id=125463">STRESSED ASSETS RECOVERY ...</a>
<a href="bankdetails.jsp?bank_id=12643">SULTAN BATHERY</a>
<a href="bankdetails.jsp?bank_id=125510">TECHNO VALLEY (TRIVANDRUM...</a>
<a href="bankdetails.jsp?bank_id=12646">TELLICHERRY</a>
<a href="bankdetails.jsp?bank_id=140273">THAMARASSERY</a>
<a href="bankdetails.jsp?bank_id=12648">THAMPANOOR</a>
<a href="bankdetails.jsp?bank_id=12650">THATTATHUMALA</a>
<a href="bankdetails.jsp?bank_id=128738">THEVALLY</a>
<a href="bankdetails.jsp?bank_id=12652">THIDANAD</a>
<a href="bankdetails.jsp?bank_id=12654">THIRUVALLA</a>
<a href="bankdetails.jsp?bank_id=12656">THIRUVANNUR</a>
<a href="bankdetails.jsp?bank_id=125460">THRIKKAKARA</a>
<a href="bankdetails.jsp?bank_id=12659">THURAVU</a>
<a href="bankdetails.jsp?bank_id=12661">TIRUR TOWN</a>
<a href="bankdetails.jsp?bank_id=12662">TREASURY</a>
<a href="bankdetails.jsp?bank_id=12664">TRICHUR TOWN</a>
<a href="bankdetails.jsp?bank_id=125444">TRIPUNITHURA</a>
<a href="bankdetails.jsp?bank_id=12667">UDUMBANNOOR</a>
<a href="bankdetails.jsp?bank_id=140271">UPPALA</a>
<a href="bankdetails.jsp?bank_id=121032">VADAKKANTHARA</a>
<a href="bankdetails.jsp?bank_id=125414">VADUVANCHAL</a>
<a href="bankdetails.jsp?bank_id=125422">VALANCHERRY</a>
<a href="bankdetails.jsp?bank_id=12671">VALIATHURA</a>
<a href="bankdetails.jsp?bank_id=12673">VALLACHIRA</a>
<a href="bankdetails.jsp?bank_id=154517">VALLUVAMBRAM</a>
<a href="bankdetails.jsp?bank_id=12675">VANIYAMKULAM</a>
<a href="bankdetails.jsp?bank_id=12676">VARAPETTY</a>
<a href="bankdetails.jsp?bank_id=125509">VATTAPARA</a>
<a href="bankdetails.jsp?bank_id=12679">VECHUCHIRA</a>
<a href="bankdetails.jsp?bank_id=125505">VELI HILLS THUMBA</a>
<a href="bankdetails.jsp?bank_id=12681">VELLOOR</a>
<a href="bankdetails.jsp?bank_id=12683">VENMONY</a>
<a href="bankdetails.jsp?bank_id=12684">VILANGAN</a>
<a href="bankdetails.jsp?bank_id=12686">WILLINGDON ISLAND</a>
<a href="bankdetails.jsp?bank_id=112073">ADOOR BRANCH</a>
<a href="bankdetails.jsp?bank_id=97485">ALAPPUZHA - KERALA</a>
<a href="bankdetails.jsp?bank_id=112303">ANGAMALLY BRANCH</a>
<a href="bankdetails.jsp?bank_id=112314">BENDICHAL SHOPPING ARCADE...</a>
<a href="bankdetails.jsp?bank_id=112323">C V M COMPLEX/ VADAKKENCH...</a>
<a href="bankdetails.jsp?bank_id=81260">CALICUT</a>
<a href="bankdetails.jsp?bank_id=81262">CHALAKUDY</a>
<a href="bankdetails.jsp?bank_id=112286">CHANGANACHERRY</a>
<a href="bankdetails.jsp?bank_id=81271">CHENGANNUR-ALAPPUZHA</a>
<a href="bankdetails.jsp?bank_id=112282">CHURCH BUILDINGS/ PALLICH...</a>
<a href="bankdetails.jsp?bank_id=81292">COCHIN - BANNERJI ROAD</a>
<a href="bankdetails.jsp?bank_id=101052">COCHIN - KALAMASSERY</a>
<a href="bankdetails.jsp?bank_id=81293">COCHIN - RAVIPURAM</a>
<a href="bankdetails.jsp?bank_id=112337">CRESCENT AUDITIORIUM/PERI...</a>
<a href="bankdetails.jsp?bank_id=112012">DARRAGH SMAIL CENTRE</a>
<a href="bankdetails.jsp?bank_id=112298">DEVASWOM NADA</a>
<a href="bankdetails.jsp?bank_id=112333">DOOR 1V/274/KOTTAPURAM</a>
<a href="bankdetails.jsp?bank_id=112304">DR.MENEZES BUILDINGS/ PAL...</a>
<a href="bankdetails.jsp?bank_id=112076">EDAPALLY</a>
<a href="bankdetails.jsp?bank_id=112300">ERNAKULUM</a>
<a href="bankdetails.jsp?bank_id=112023">GURUVAYOOR BRANCH X/83 A/...</a>
<a href="bankdetails.jsp?bank_id=81373">IRINJALAKUDA</a>
<a href="bankdetails.jsp?bank_id=112321">JRJ COMPLEX/ MAIN ROAD/ O...</a>
<a href="bankdetails.jsp?bank_id=112301">KALOOR JUNCTION</a>
<a href="bankdetails.jsp?bank_id=112315">KANHANGAD BRANCH</a>
<a href="bankdetails.jsp?bank_id=112295">KARIMPANAL ARCADE</a>
<a href="bankdetails.jsp?bank_id=101044">KAZHAKKOOTA - TRIVANDRUM</a>
<a href="bankdetails.jsp?bank_id=97567">KOCHI - PARAVUR</a>
<a href="bankdetails.jsp?bank_id=112319">KODUVAYUR - KERALA</a>
<a href="bankdetails.jsp?bank_id=81428">KOLLAM</a>
<a href="bankdetails.jsp?bank_id=81431">KOTTAYAM</a>
<a href="bankdetails.jsp?bank_id=112288">KUDAMALOOR - KERALA</a>
<a href="bankdetails.jsp?bank_id=112299">KURIAN TOWERS</a>
<a href="bankdetails.jsp?bank_id=112383">KUTHAMPULLY - KERALA</a>
<a href="bankdetails.jsp?bank_id=112334">LOKAMALLESWARAM - KERALA</a>
<a href="bankdetails.jsp?bank_id=112008">MAIN BRANCH CHOICE TOWERS</a>
<a href="bankdetails.jsp?bank_id=112335">MALA - PADAYATTI COMPLEX</a>
<a href="bankdetails.jsp?bank_id=112320">MALUAMMA MEMORIAL BUILDIN...</a>
<a href="bankdetails.jsp?bank_id=146607">MATTANNUR</a>
<a href="bankdetails.jsp?bank_id=112276">MAVELIKKARA - KERALA</a>
<a href="bankdetails.jsp?bank_id=112275">MUVATTUPUZHA</a>
<a href="bankdetails.jsp?bank_id=112297">NAIR SAMAJAM BUILDINGS</a>
<a href="bankdetails.jsp?bank_id=112045">NEAR BABY MEMORIAL HOSPIT...</a>
<a href="bankdetails.jsp?bank_id=112291">ORAVAKKAL BUILDINGS/AMAYA...</a>
<a href="bankdetails.jsp?bank_id=81592">PALAKKAD</a>
<a href="bankdetails.jsp?bank_id=112281">PANCHAYATH SHOPP COMP./ N...</a>
<a href="bankdetails.jsp?bank_id=81599">PATHANAMTHITTA</a>
<a href="bankdetails.jsp?bank_id=112308">PEPPATHY JUNCTION/ VELIAY...</a>
<a href="bankdetails.jsp?bank_id=112307">PERUMBAVOOR</a>
<a href="bankdetails.jsp?bank_id=112338">PUTHENCHIRA - MANGIDIYAN ...</a>
<a href="bankdetails.jsp?bank_id=112292">PUZHAKKARAYIL BUILDINGS/T...</a>
<a href="bankdetails.jsp?bank_id=112279">RAJA MAHAL BUILDINGS/ CHE...</a>
<a href="bankdetails.jsp?bank_id=112340">RENUKA COMPLEX - THIRUVIL...</a>
<a href="bankdetails.jsp?bank_id=112388">SASTHAMANGALAM</a>
<a href="bankdetails.jsp?bank_id=112318">SICO TOWERS - CHERPALACHE...</a>
<a href="bankdetails.jsp?bank_id=112339">SREENARAYANAN SAMAJAM/SHO...</a>
<a href="bankdetails.jsp?bank_id=112091">ST THOMAS CATHEDRAL COMPL...</a>
<a href="bankdetails.jsp?bank_id=112049">SUDHARSHA TOWERS</a>
<a href="bankdetails.jsp?bank_id=112313">TELLICHERRY</a>
<a href="bankdetails.jsp?bank_id=112390">THRIKKAKARA</a>
<a href="bankdetails.jsp?bank_id=81677">TIRUVALLA - M C ROAD</a>
<a href="bankdetails.jsp?bank_id=97568">TRICHUR - CHERPU</a>
<a href="bankdetails.jsp?bank_id=81678">TRICHUR - PALACE ROAD</a>
<a href="bankdetails.jsp?bank_id=81681">TRIVANDRUM - PONGUMOODU -...</a>
<a href="bankdetails.jsp?bank_id=112306">UDAYAMPEROOR/ SOUTH PARUR</a>
<a href="bankdetails.jsp?bank_id=154620">VATTIYURKAVU</a>
<a href="bankdetails.jsp?bank_id=80046">Alapuzha</a>
<a href="bankdetails.jsp?bank_id=79721">Calicut</a>
<a href="bankdetails.jsp?bank_id=79734">Ernakulam</a>
<a href="bankdetails.jsp?bank_id=80155">Kalpeta</a>
<a href="bankdetails.jsp?bank_id=80130">Kannur</a>
<a href="bankdetails.jsp?bank_id=80118">Kottayam</a>
<a href="bankdetails.jsp?bank_id=79759">Palghat</a>
<a href="bankdetails.jsp?bank_id=80145">Pathanamthitta</a>
<a href="bankdetails.jsp?bank_id=79881">Quilon</a>
<a href="bankdetails.jsp?bank_id=80092">Thiruvalla</a>
<a href="bankdetails.jsp?bank_id=80139">Tirur</a>
<a href="bankdetails.jsp?bank_id=79944">Trivandrum</a>
<a href="bankdetails.jsp?bank_id=154270">ADOOR</a>
<a href="bankdetails.jsp?bank_id=95918">ALUVA (KERALA)</a>
<a href="bankdetails.jsp?bank_id=104272">ATTINGAL</a>
<a href="bankdetails.jsp?bank_id=154397">CHANGANASSERI</a>
<a href="bankdetails.jsp?bank_id=154648">EAST FORT, THRISSUR</a>
<a href="bankdetails.jsp?bank_id=137770">KALAMASERRY</a>
<a href="bankdetails.jsp?bank_id=154156">KALOOR, KOCHI</a>
<a href="bankdetails.jsp?bank_id=87114">KANNUR</a>
<a href="bankdetails.jsp?bank_id=104090">KASARGOD/ KERALA</a>
<a href="bankdetails.jsp?bank_id=93581">KOCHI</a>
<a href="bankdetails.jsp?bank_id=137638">KOTTAKKAL</a>
<a href="bankdetails.jsp?bank_id=91269">KOTTAYAM</a>
<a href="bankdetails.jsp?bank_id=91276">MALAPPURAM</a>
<a href="bankdetails.jsp?bank_id=104344">MAVELIKKARA</a>
<a href="bankdetails.jsp?bank_id=104257">PALAI/ KERALA</a>
<a href="bankdetails.jsp?bank_id=137676">PANAMPILLY NAGAR, KOCHI</a>
<a href="bankdetails.jsp?bank_id=137006">PAYYANNUR</a>
<a href="bankdetails.jsp?bank_id=137636">RAVIPURAM,KOCHI</a>
<a href="bankdetails.jsp?bank_id=119566">SULTHANBATHERY </a>
<a href="bankdetails.jsp?bank_id=95052">THIRUVALLA KERALA</a>
<a href="bankdetails.jsp?bank_id=95041">THODUPUZHA [ KERALA ]</a>
<a href="bankdetails.jsp?bank_id=119585">THRIPPUNITHURA</a>
<a href="bankdetails.jsp?bank_id=137742">TIRUR</a>
<a href="bankdetails.jsp?bank_id=104383">VYTILLA/ KOCHI</a>
<a href="bankdetails.jsp?bank_id=112961">ADOOR</a>
<a href="bankdetails.jsp?bank_id=112952">ANGAMALY</a>
<a href="bankdetails.jsp?bank_id=139040">AROOR</a>
<a href="bankdetails.jsp?bank_id=112964">CHALAKUDY</a>
<a href="bankdetails.jsp?bank_id=138888">CHEMBUMUKKU- KOCHI, KERAL...</a>
<a href="bankdetails.jsp?bank_id=119494">CHERTALA/ KERALA</a>
<a href="bankdetails.jsp?bank_id=81861">East Bazaar - Tirur </a>
<a href="bankdetails.jsp?bank_id=138892">EDAPPAL, KERALA</a>
<a href="bankdetails.jsp?bank_id=139069">ERANKULAM PALLIMUKKU</a>
<a href="bankdetails.jsp?bank_id=154416">Ettumanoor</a>
<a href="bankdetails.jsp?bank_id=113526">HARIPPAD/ KERALA </a>
<a href="bankdetails.jsp?bank_id=154621">INFOSYS - TECHNOPARK, THI...</a>
<a href="bankdetails.jsp?bank_id=113129">KAKKANAD</a>
<a href="bankdetails.jsp?bank_id=154417">KALATHIPADY</a>
<a href="bankdetails.jsp?bank_id=112967">KALPETTA</a>
<a href="bankdetails.jsp?bank_id=112956">KANJIRAPPALLY</a>
<a href="bankdetails.jsp?bank_id=88546">Kannur / Cannanore </a>
<a href="bankdetails.jsp?bank_id=81714">Kasaragod </a>
<a href="bankdetails.jsp?bank_id=138999">KAYAMKULLAM, KERALA</a>
<a href="bankdetails.jsp?bank_id=113238">KOCHI</a>
<a href="bankdetails.jsp?bank_id=154190">KOCHI - JAWAHAR NAGAR KER...</a>
<a href="bankdetails.jsp?bank_id=138889">KOCHI - WELLINGTON ISLAND...</a>
<a href="bankdetails.jsp?bank_id=81731">Kollam (Quilon) </a>
<a href="bankdetails.jsp?bank_id=113150">KOTHAMANGALAM</a>
<a href="bankdetails.jsp?bank_id=113199">KOTTARAKKARA</a>
<a href="bankdetails.jsp?bank_id=81732">Kottayam </a>
<a href="bankdetails.jsp?bank_id=82120">Kozhikode (Calicut) </a>
<a href="bankdetails.jsp?bank_id=112815">KOZHIKODE - KALLAI ROAD</a>
<a href="bankdetails.jsp?bank_id=81734">Kumbanad </a>
<a href="bankdetails.jsp?bank_id=112966">KUNNAMKULAM/ KERALA</a>
<a href="bankdetails.jsp?bank_id=119699">MANACAUD - THIRUVANANTHAP...</a>
<a href="bankdetails.jsp?bank_id=113504">MANNARKAD </a>
<a href="bankdetails.jsp?bank_id=82121">MC Road Thiruvalla </a>
<a href="bankdetails.jsp?bank_id=154622">NEDUMANGAD</a>
<a href="bankdetails.jsp?bank_id=112960">NILAMBUR</a>
<a href="bankdetails.jsp?bank_id=112847">OTTAPPALAM</a>
<a href="bankdetails.jsp?bank_id=154573">PANDALAM</a>
<a href="bankdetails.jsp?bank_id=113590">PATTOM-THIRUVANANTHAPURAM...</a>
<a href="bankdetails.jsp?bank_id=112953">PERUMBAVOOR</a>
<a href="bankdetails.jsp?bank_id=154364">PUNALUR KERELA</a>
<a href="bankdetails.jsp?bank_id=113498">PUZHAKKAL /THRISSUR</a>
<a href="bankdetails.jsp?bank_id=113505">RANNI/ KERALA</a>
<a href="bankdetails.jsp?bank_id=119488">SASTHAMANGALAM/ THIRUVANA...</a>
<a href="bankdetails.jsp?bank_id=81859">T.K. Road, Pathanamtitha </a>
<a href="bankdetails.jsp?bank_id=94873">THALASSARY</a>
<a href="bankdetails.jsp?bank_id=82119">Thiruvananthapuram (Triva...</a>
<a href="bankdetails.jsp?bank_id=112954">THODUPUZHA</a>
<a href="bankdetails.jsp?bank_id=138903">THRISSUR - 2, KERALA</a>
<a href="bankdetails.jsp?bank_id=78048">TRIVANDRUM - KOWDIAR</a>
<a href="bankdetails.jsp?bank_id=112764">TRIVANDRUM - PAZHAYA ROAD...</a>
<a href="bankdetails.jsp?bank_id=113539">VARKALA/ KERALA</a>
<a href="bankdetails.jsp?bank_id=138863">VYTILA, ERNAKULAM</a>
<a href="bankdetails.jsp?bank_id=114177"> KOLLAM</a>
<a href="bankdetails.jsp?bank_id=4127">ALAPPUZHA</a>
<a href="bankdetails.jsp?bank_id=4129">AMBALATHARA</a>
<a href="bankdetails.jsp?bank_id=113999">ANGAMALI</a>
<a href="bankdetails.jsp?bank_id=4131">ATTINGAL</a>
<a href="bankdetails.jsp?bank_id=4132">BALARAMAPURAM</a>
<a href="bankdetails.jsp?bank_id=114011">BHARANIKKAVVU</a>
<a href="bankdetails.jsp?bank_id=4136">CHALAI</a>
<a href="bankdetails.jsp?bank_id=4138">CHANGANASSERY</a>
<a href="bankdetails.jsp?bank_id=114045">CHENGAMANAD (KOLLAM)</a>
<a href="bankdetails.jsp?bank_id=136920">CHERTHALA</a>
<a href="bankdetails.jsp?bank_id=4142">CHITARA</a>
<a href="bankdetails.jsp?bank_id=4143">ERNAKULAM</a>
<a href="bankdetails.jsp?bank_id=4144">GURUVAYOOR</a>
<a href="bankdetails.jsp?bank_id=4145">ITTIVA</a>
<a href="bankdetails.jsp?bank_id=114172">KAITHACODE</a>
<a href="bankdetails.jsp?bank_id=154195">KALAMASSERY</a>
<a href="bankdetails.jsp?bank_id=114191">KALPETTA</a>
<a href="bankdetails.jsp?bank_id=4151">KANNUR</a>
<a href="bankdetails.jsp?bank_id=4152">KARUNAGAPALLY</a>
<a href="bankdetails.jsp?bank_id=139335">KAYAMKULAM</a>
<a href="bankdetails.jsp?bank_id=4155">KERALAPURAM</a>
<a href="bankdetails.jsp?bank_id=4157">KODUNGALLUR</a>
<a href="bankdetails.jsp?bank_id=4160">KOTTAYAM</a>
<a href="bankdetails.jsp?bank_id=4161">KOZHENCHERRY</a>
<a href="bankdetails.jsp?bank_id=4163">KUNNAMKULAM</a>
<a href="bankdetails.jsp?bank_id=4164">M O ROAD</a>
<a href="bankdetails.jsp?bank_id=139373">MANJERI</a>
<a href="bankdetails.jsp?bank_id=4167">MAYYANAD</a>
<a href="bankdetails.jsp?bank_id=114276">MICROSATE/ THIRUVANANTHAP...</a>
<a href="bankdetails.jsp?bank_id=4169">NALANCHIRA</a>
<a href="bankdetails.jsp?bank_id=4171">NIRANAM</a>
<a href="bankdetails.jsp?bank_id=114299">NRI RANNI</a>
<a href="bankdetails.jsp?bank_id=114315">PALA</a>
<a href="bankdetails.jsp?bank_id=4175">PALLICKAL</a>
<a href="bankdetails.jsp?bank_id=4177">PAPPINISSERI</a>
<a href="bankdetails.jsp?bank_id=4179">PARAVUR</a>
<a href="bankdetails.jsp?bank_id=4180">PATHANAMTHITTA</a>
<a href="bankdetails.jsp?bank_id=4181">PATTOM</a>
<a href="bankdetails.jsp?bank_id=114478">PERUMBAVOOR</a>
<a href="bankdetails.jsp?bank_id=4183">PIRAYIRI</a>
<a href="bankdetails.jsp?bank_id=4184">PUDUNAGARAM</a>
<a href="bankdetails.jsp?bank_id=4186">PUTHUR</a>
<a href="bankdetails.jsp?bank_id=4188">SASTHAMKOTTA</a>
<a href="bankdetails.jsp?bank_id=114410">THEVALAKKARA</a>
<a href="bankdetails.jsp?bank_id=4192">THIRUVANANTHAPURAM</a>
<a href="bankdetails.jsp?bank_id=114417">THOLICODE</a>
<a href="bankdetails.jsp?bank_id=4195">THRISSUR</a>
<a href="bankdetails.jsp?bank_id=139418">TIRUR</a>
<a href="bankdetails.jsp?bank_id=4199">VADAKARAPATHY</a>
<a href="bankdetails.jsp?bank_id=4200">VAVVAKKAVU</a>
<a href="bankdetails.jsp?bank_id=4202">WILLINGTON ISLAND</a>
<a href="bankdetails.jsp?bank_id=78855">CHENGANNUR</a>
<a href="bankdetails.jsp?bank_id=84504">Ernakulam Branch</a>
<a href="bankdetails.jsp?bank_id=93363">KOZHIKODE(CALICUT)</a>
<a href="bankdetails.jsp?bank_id=93246">THIRUVANANTHAPURAM</a>
<a href="bankdetails.jsp?bank_id=93369">TIRUVELLA</a>
<a href="bankdetails.jsp?bank_id=93365">VENNELA(ERNAKULAM)</a>
<a href="bankdetails.jsp?bank_id=103517">VYTTILA(KOCHI)</a>
<a href="bankdetails.jsp?bank_id=104051">WILLINGDON ISLAND</a>
<a href="bankdetails.jsp?bank_id=80720">Cochin</a>
<a href="bankdetails.jsp?bank_id=112389">VIYYOOR BRANCH</a>
<a href="bankdetails.jsp?bank_id=99332">KOCHI</a>
<a href="bankdetails.jsp?bank_id=99333">TRIVANDRUM</a>
<a href="bankdetails.jsp?bank_id=81890">WEST FORT ROAD -  Palakka...</a>
<a href="bankdetails.jsp?bank_id=137148">ULLOOR</a>
<a href="bankdetails.jsp?bank_id=4202">WILLINGTON ISLAND</a>
<a href="bankdetails.jsp?bank_id=140892">YMCA JUNCTION, ERNAKULAM</a></html>'''

page = urllib.urlopen(urls)
html = page.read()    
soup=BeautifulSoup(html)
links=soup.find('a')
