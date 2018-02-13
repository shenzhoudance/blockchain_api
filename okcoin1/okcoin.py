#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
#客户端调用，用于查看API返回结果

from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture
import ssl
import csv
import datetime
import time
from multiprocessing import Pool
from SaveMysql import updateMysql,insertMysql

ssl._create_default_https_context = ssl._create_unverified_context

#初始化apikey，secretkey,url
apikey = 'a5f678c4-c234-4a17-a21a-ed218b6c7f51'
secretkey = '5BE848BE3E6C300292F1F06C9DA00180'
okcoinRESTURL = 'www.okex.com'   #请求注意：国内账号需要 修改为 www.okcoin.cn

#现货API
okcoinSpot = OKCoinSpot(okcoinRESTURL,apikey,secretkey)

#期货API
okcoinFuture = OKCoinFuture(okcoinRESTURL,apikey,secretkey)

print (u' 现货行情 ')
#print (okcoinSpot.ticker('btc_usd'))

print (u' 现货深度 ')
#print (okcoinSpot.depth('btc_usd'))
eos_eth = okcoinSpot.depth('eos_eth')
print('asks')
print (eos_eth['asks'])
print('bids')
print (eos_eth['bids'])


def save_mysql_get_depth(symbol):
    symbolname = symbol
    symbol = symbolname.replace('_', '')
    platForm = 'okex'
    filednames = ['symbol', 'platform', 'datetime', 'priceAverage', 'buyPrice', 'bNum', 'sellPrice', 'sNum',
                  'allInfo']
    while(1):
        try:
            symbolprice = okcoinSpot.depth(symbolname)
            print(symbolname)
            updateMysql(symbol,'okex',str((symbolprice['asks'][-1][0] + symbolprice['bids'][0][0]) * 0.5),str(symbolprice['bids'][0][0]),str(symbolprice['bids'][0][1]),str(symbolprice['asks'][-1][0]),str(symbolprice['asks'][-1][1]),str(symbolprice))
        except:
            pass

all_symbol = ['ltc_btc','eth_btc','etc_btc','bch_btc','xrp_btc','xem_btc','xlm_btc','iota_btc','1st_btc','aac_btc','ace_btc','act_btc','aidoc_btc','amm_btc','ark_btc','ast_btc','atl_btc','avt_btc','bcd_btc','bcx_btc','bnt_btc','brd_btc','bt2_btc','btg_btc','btm_btc','cag_btc','can_btc','cbt_btc','chat_btc','cic_btc','cmt_btc','ctr_btc','cvc_btc','dash_btc','dat_btc','dent_btc','dgd_btc','dna_btc','dnt_btc','dpy_btc','edo_btc','elf_btc','eng_btc','eos_btc','evx_btc','fair_btc','fun_btc','gas_btc','gnt_btc','gnx_btc','gto_btc','hmc_btc','hot_btc','hsr_btc','icn_btc','icx_btc','ins_btc','insur_btc','int_btc','iost_btc','ipc_btc','itc_btc','kcash_btc','key_btc','knc_btc','la_btc','lend_btc','lev_btc','light_btc','link_btc','lrc_btc','mag_btc','mana_btc','mof_btc','mot_btc','mth_btc','mtl_btc','nano_btc','nas_btc','neo_btc','ngc_btc','nuls_btc','oax_btc','of_btc','omg_btc','ost_btc','pay_btc','poe_btc','ppt_btc','prt_btc','pra_btc','pst_btc','qtum_btc','qun_btc','qvt_btc','r_btc','rcn_btc','rct_btc','rdn_btc','read_btc','ref_btc','req_btc','rnt_btc','salt_btc','san_btc','sbtc_btc','show_btc','smt_btc','snc_btc','sngls_btc','snm_btc','snt_btc','soc_btc','spf_btc','ssc_btc','stc_btc','storj_btc','sub_btc','swftc_btc','tct_btc','theta_btc','tio_btc','tnb_btc','topc_btc','true_btc','trx_btc','ubtc_btc','uct_btc','ugc_btc','ukg_btc','utk_btc','vee_btc','vib_btc','viu_btc','wbtc_btc','wrc_btc','wtc_btc','xmr_btc','xuc_btc','yee_btc','yoyo_btc','zec_btc','zen_btc','zip_btc','zrx_btc',
                'ltc_eth','eth_eth','etc_eth','bch_eth','xrp_eth','xem_eth','xlm_eth','iota_eth','1st_eth','aac_eth','ace_eth','act_eth','aidoc_eth','amm_eth','ark_eth','ast_eth','atl_eth','avt_eth','bcd_eth','bcx_eth','bnt_eth','brd_eth','bt2_eth','btg_eth','btm_eth','cag_eth','can_eth','cbt_eth','chat_eth','cic_eth','cmt_eth','ctr_eth','cvc_eth','dash_eth','dat_eth','dent_eth','dgd_eth','dna_eth','dnt_eth','dpy_eth','edo_eth','elf_eth','eng_eth','eos_eth','evx_eth','fair_eth','fun_eth','gas_eth','gnt_eth','gnx_eth','gto_eth','hmc_eth','hot_eth','hsr_eth','icn_eth','icx_eth','ins_eth','insur_eth','int_eth','iost_eth','ipc_eth','itc_eth','kcash_eth','key_eth','knc_eth','la_eth','lend_eth','lev_eth','light_eth','link_eth','lrc_eth','mag_eth','mana_eth','mof_eth','mot_eth','mth_eth','mtl_eth','nano_eth','nas_eth','neo_eth','ngc_eth','nuls_eth','oax_eth','of_eth','omg_eth','ost_eth','pay_eth','poe_eth','ppt_eth','prt_eth','pra_eth','pst_eth','qtum_eth','qun_eth','qvt_eth','r_eth','rcn_eth','rct_eth','rdn_eth','read_eth','ref_eth','req_eth','rnt_eth','salt_eth','san_eth','sbtc_eth','show_eth','smt_eth','snc_eth','sngls_eth','snm_eth','snt_eth','soc_eth','spf_eth','ssc_eth','stc_eth','storj_eth','sub_eth','swftc_eth','tct_eth','theta_eth','tio_eth','tnb_eth','topc_eth','true_eth','trx_eth','ubtc_eth','uct_eth','ugc_eth','ukg_eth','utk_eth','vee_eth','vib_eth','viu_eth','wbtc_eth','wrc_eth','wtc_eth','xmr_eth','xuc_eth','yee_eth','yoyo_eth','zec_eth','zen_eth','zip_eth','zrx_eth',
                'btc_usdt','ltc_usdt','eth_usdt','etc_usdt','bch_usdt','xrp_usdt','xem_usdt','xlm_usdt','iota_usdt','1st_usdt','aac_usdt','ace_usdt','act_usdt','aidoc_usdt','amm_usdt','ark_usdt','ast_usdt','atl_usdt','avt_usdt','bcd_usdt','bcx_usdt','bnt_usdt','brd_usdt','bt2_usdt','btg_usdt','btm_usdt','cag_usdt','can_usdt','cbt_usdt','chat_usdt','cic_usdt','cmt_usdt','ctr_usdt','cvc_usdt','dash_usdt','dat_usdt','dent_usdt','dgd_usdt','dna_usdt','dnt_usdt','dpy_usdt','edo_usdt','elf_usdt','eng_usdt','eos_usdt','evx_usdt','fair_usdt','fun_usdt','gas_usdt','gnt_usdt','gnx_usdt','gto_usdt','hmc_usdt','hot_usdt','hsr_usdt','icn_usdt','icx_usdt','ins_usdt','insur_usdt','int_usdt','iost_usdt','ipc_usdt','itc_usdt','kcash_usdt','key_usdt','knc_usdt','la_usdt','lend_usdt','lev_usdt','light_usdt','link_usdt','lrc_usdt','mag_usdt','mana_usdt','mof_usdt','mot_usdt','mth_usdt','mtl_usdt','nano_usdt','nas_usdt','neo_usdt','ngc_usdt','nuls_usdt','oax_usdt','of_usdt','omg_usdt','ost_usdt','pay_usdt','poe_usdt','ppt_usdt','prt_usdt','pra_usdt','pst_usdt','qtum_usdt','qun_usdt','qvt_usdt','rcn_usdt','rct_usdt','rdn_usdt','read_usdt','ref_usdt','req_usdt','rnt_usdt','salt_usdt','san_usdt','sbtc_usdt','show_usdt','smt_usdt','snc_usdt','sngls_usdt','snm_usdt','snt_usdt','soc_usdt','spf_usdt','ssc_usdt','stc_usdt','storj_usdt','sub_usdt','swftc_usdt','tct_usdt','theta_usdt','tio_usdt','tnb_usdt','topc_usdt','true_usdt','trx_usdt','ubtc_usdt','uct_usdt','ugc_usdt','ukg_usdt','utk_usdt','vee_usdt','vib_usdt','viu_usdt','wbtc_usdt','wrc_usdt','wtc_usdt','xmr_usdt','xuc_usdt','yee_usdt','yoyo_usdt','zec_usdt','zen_usdt','zip_usdt','zrx_usdt',
                'ltc_bch','etc_bch','act_bch','avt_bch','bcd_bch','bcx_bch','cmt_bch','dash_bch','eos_bch','sbtc_bch','btg_bch','r_usdt','dgd_bch','edo_bch'
                 ]



#insertMysql(symbol,platform,priceAverage,buyprice='NULL',bNum='NULL',sellPrice='NULL',sNum='NULL',allInfo='NULL')
# for N in all_symbol:
#     N = N.replace('_','')
#     insertMysql(N,'okex','0')
# for N in all_symbol:
#     symbolPrice = okcoinSpot.depth(N)
#     print(N,symbolPrice)
if __name__ == '__main__':
    with Pool(200) as p:
        p.map(save_mysql_get_depth, all_symbol)


# print (okcoinSpot.depth('ltc_btc'))
# all_symbol = 'ltc_btc eth_btc etc_btc bch_btc btc_usdt eth_usdt ltc_usdt etc_usdt bch_usdt etc_eth bt1_btc bt2_btc btg_btc qtum_btc hsr_btc neo_btc gas_btc qtum_usdt hsr_usdt neo_usdt gas_usdt'
# all_symbol_new = all_symbol.split(' ')
# print(all_symbol_new)
# for N in all_symbol_new:
#     print(okcoinSpot.depth(N))


#print (u' 现货历史交易信息 ')
#print (okcoinSpot.trades())

#print (u' 用户现货账户信息 ')
#print (okcoinSpot.userinfo())

#print (u' 现货下单 ')
#print (okcoinSpot.trade('ltc_usd','buy','0.1','0.2'))

#print (u' 现货批量下单 ')
#print (okcoinSpot.batchTrade('ltc_usd','buy','[{price:0.1,amount:0.2},{price:0.1,amount:0.2}]'))

#print (u' 现货取消订单 ')
#print (okcoinSpot.cancelOrder('ltc_usd','18243073'))

#print (u' 现货订单信息查询 ')
#print (okcoinSpot.orderinfo('ltc_usd','18243644'))

#print (u' 现货批量订单信息查询 ')
#print (okcoinSpot.ordersinfo('ltc_usd','18243800,18243801,18243644','0'))

#print (u' 现货历史订单信息查询 ')
#print (okcoinSpot.orderHistory('ltc_usd','0','1','2'))

#print (u' 期货行情信息')
#print (okcoinFuture.future_ticker('ltc_usd','this_week'))

#print (u' 期货市场深度信息')
#print (okcoinFuture.future_depth('btc_usd','this_week','6'))

#print (u'期货交易记录信息') 
#print (okcoinFuture.future_trades('ltc_usd','this_week'))

#print (u'期货指数信息')
#print (okcoinFuture.future_index('ltc_usd'))

#print (u'美元人民币汇率')
#print (okcoinFuture.exchange_rate())

#print (u'获取预估交割价') 
#print (okcoinFuture.future_estimated_price('ltc_usd'))

#print (u'获取全仓账户信息')
#print (okcoinFuture.future_userinfo())

#print (u'获取全仓持仓信息')
#print (okcoinFuture.future_position('ltc_usd','this_week'))

#print (u'期货下单')
#print (okcoinFuture.future_trade('ltc_usd','this_week','0.1','1','1','0','20'))

#print (u'期货批量下单')
#print (okcoinFuture.future_batchTrade('ltc_usd','this_week','[{price:0.1,amount:1,type:1,match_price:0},{price:0.1,amount:3,type:1,match_price:0}]','20'))

#print (u'期货取消订单')
#print (okcoinFuture.future_cancel('ltc_usd','this_week','47231499'))

#print (u'期货获取订单信息')
#print (okcoinFuture.future_orderinfo('ltc_usd','this_week','47231812','0','1','2'))

#print (u'期货逐仓账户信息')
#print (okcoinFuture.future_userinfo_4fix())

#print (u'期货逐仓持仓信息')
#print (okcoinFuture.future_position_4fix('ltc_usd','this_week',1))





    ### save csv
    # with open('../huobi.csv', 'r', ) as huobifile:
    #     reader = csv.DictReader(huobifile)
    #     temp_dict ={}
    #     for row in reader:
    #         temp_dict[row['symbol'] + row['platform']] = [row['symbol'], row['platform'],
    #                           row['datetime'],
    #                           row['priceAverage'],
    #                           row['buyPrice'],
    #                           row['bNum'],
    #                           row['sellPrice'],
    #                           row['sNum'],
    #                           row['allInfo']]

    #     symbolTrue = symbol + platForm
    #
    # if symbolTrue in temp_dict:
    #     temp_dict[symbolTrue] = [symbol, platForm,
    #                              datetime.datetime.now(),
    #                              str((symbolprice['asks'][-1][0] + symbolprice['bids'][0][0]) * 0.5),
    #                              symbolprice['bids'][0][0], symbolprice['bids'][0][1],
    #                              symbolprice['asks'][-1][0], symbolprice['asks'][-1][1],
    #                              symbolprice]
    #
    #     with open('../huobi.csv', 'w', ) as huobifile:
    #         csvwriter = csv.DictWriter(huobifile, fieldnames=filednames)
    #         csvwriter.writeheader()
    #         for name, key in temp_dict.items():
    #             csvwriterValue = {'symbol': key[0], 'platform': key[1], 'datetime': key[2], 'priceAverage': key[3],
    #                               'buyPrice': key[4], 'bNum': key[5], 'sellPrice': key[6], 'sNum': key[7],
    #                               'allInfo': key[8]}
    #             csvwriter.writerow(csvwriterValue)
    # else:
    #     with open('../huobi.csv', 'a', ) as huobifile:
    #         csvwriter = csv.DictWriter(huobifile, fieldnames=filednames)
    #         csvwriterValue = {'datetime': datetime.datetime.now(), 'platform': platForm, 'symbol': symbol}
    #         csvwriterValue['priceAverage'] = str((symbolprice['asks'][-1][0] + symbolprice['bids'][0][0]) * 0.5),
    #         csvwriterValue['buyPrice'] = symbolprice['bids'][0][0]
    #         csvwriterValue['bNum'] = symbolprice['bids'][0][1]
    #         csvwriterValue['sellPrice'] = symbolprice['asks'][-1][0]
    #         csvwriterValue['sNum'] = symbolprice['asks'][-1][1]
    #         csvwriterValue['allInfo'] = symbolprice
    #         csvwriter.writerow(csvwriterValue)
    #         # -- save data -- #


# okex symbol

# okexSymbolValue = 'ltc_btc,eth_btc,etc_btc,bch_btc,xrp_btc,xem_btc,xlm_btc,iota_btc,1st_btc,aac_btc,ace_btc,act_btc,aidoc_btc,amm_btc,ark_btc,ast_btc,atl_btc,avt_btc,bcd_btc,bcx_btc,bnt_btc,brd_btc,bt2_btc,btg_btc,btm_btc,cag_btc,can_btc,cmt_btc,ctr_btc,cvc_btc,dash_btc,dat_btc,dgb_btc,dgd_btc,dna_btc,dnt_btc,dpy_btc,edo_btc,elf_btc,eng_btc,eos_btc,evx_btc,fair_btc,fun_btc,gas_btc,gnt_btc,gnx_btc,hot_btc,hsr_btc,icn_btc,icx_btc,ins_btc,int_btc,iost_btc,ipc_btc,itc_btc,kcash_btc,key_btc,knc_btc,la_btc,lend_btc,lev_btc,light_btc,link_btc,lrc_btc,mag_btc,mana_btc,mco_btc,mda_btc,mdt_btc,mkr_btc,mof_btc,mot_btc,mth_btc,mtl_btc,nas_btc,neo_btc,ngc_btc,nuls_btc,oax_btc,of_btc,omg_btc,ost_btc,pay_btc,poe_btc,ppt_btc,pra_btc,pst_btc,qtum_btc,qun_btc,qvt_btc,rcn_btc,rct_btc,rdn_btc,read_btc,ref_btc,req_btc,rnt_btc,salt_btc,san_btc,sbtc_btc,show_btc,smt_btc,snc_btc,sngls_btc,snm_btc,snt_btc,spf_btc,ssc_btc,stc_btc,storj_btc,sub_btc,swftc_btc,tct_btc,theta_btc,tio_btc,tnb_btc,topc_btc,true_btc,trx_btc,ubtc_btc,ugc_btc,ukg_btc,utk_btc,vee_btc,vib_btc,viu_btc,wrc_btc,wtc_btc,xmr_btc,xuc_btc,yee_btc,yoyo_btc,zec_btc,zrx_btc,btc_usdt,ltc_usdt,eth_usdt,etc_usdt,bch_usdt,xrp_usdt,xem_usdt,xlm_usdt,iota_usdt,1st_usdt,aac_usdt,ace_usdt,act_usdt,aidoc_usdt,amm_usdt,ark_usdt,ast_usdt,atl_usdt,avt_usdt,bcd_usdt,bnt_usdt,brd_usdt,btg_usdt,btm_usdt,cag_usdt,can_usdt,cmt_usdt,ctr_usdt,cvc_usdt,dash_usdt,dat_usdt,dgb_usdt,dgd_usdt,dna_usdt,dnt_usdt,dpy_usdt,edo_usdt,elf_usdt,eng_usdt,eos_usdt,evx_usdt,fair_usdt,fun_usdt,gas_usdt,gnt_usdt,gnx_usdt,hot_usdt,hsr_usdt,icn_usdt,icx_usdt,ins_usdt,int_usdt,iost_usdt,ipc_usdt,itc_usdt,kcash_usdt,key_usdt,knc_usdt,la_usdt,lend_usdt,lev_usdt,light_usdt,link_usdt,lrc_usdt,mag_usdt,mana_usdt,mco_usdt,mda_usdt,mdt_usdt,mkr_usdt,mof_usdt,mot_usdt,mth_usdt,mtl_usdt,nas_usdt,neo_usdt,ngc_usdt,nuls_usdt,oax_usdt,of_usdt,omg_usdt,ost_usdt,pay_usdt,poe_usdt,ppt_usdt,pra_usdt,pst_usdt,qtum_usdt,qun_usdt,qvt_usdt,rcn_usdt,rct_usdt,rdn_usdt,read_usdt,ref_usdt,req_usdt,rnt_usdt,salt_usdt,san_usdt,show_usdt,smt_usdt,snc_usdt,sngls_usdt,snm_usdt,snt_usdt,spf_usdt,ssc_usdt,stc_usdt,storj_usdt,sub_usdt,swftc_usdt,tct_usdt,theta_usdt,tio_usdt,tnb_usdt,topc_usdt,true_usdt,trx_usdt,ubtc_usdt,ugc_usdt,ukg_usdt,utk_usdt,vee_usdt,vib_usdt,viu_usdt,wrc_usdt,wtc_usdt,xmr_usdt,xuc_usdt,yee_usdt,yoyo_usdt,zec_usdt,zrx_usdt,ltc_bch,etc_bch,act_bch,avt_bch,bcd_bch,bcx_bch,btg_bch,cmt_bch,dash_bch,dgd_bch,edo_bch,eos_bch,sbtc_bch,ltc_eth,etc_eth,bch_eth,xrp_eth,xem_eth,xlm_eth,iota_eth,1st_eth,aac_eth,ace_eth,act_eth,aidoc_eth,amm_eth,ark_eth,ast_eth,atl_eth,avt_eth,bnt_eth,brd_eth,btm_eth,cag_eth,can_eth,cmt_eth,ctr_eth,cvc_eth,dash_eth,dat_eth,dgb_eth,dgd_eth,dna_eth,dnt_eth,dpy_eth,edo_eth,elf_eth,eng_eth,eos_eth,evx_eth,fair_eth,fun_eth,gas_eth,gnt_eth,gnx_eth,hot_eth,hsr_eth,icn_eth,icx_eth,ins_eth,int_eth,iost_eth,ipc_eth,itc_eth,kcash_eth,key_eth,knc_eth,la_eth,lend_eth,lev_eth,light_eth,link_eth,lrc_eth,mag_eth,mana_eth,mco_eth,mda_eth,mdt_eth,mkr_eth,mof_eth,mot_eth,mth_eth,mtl_eth,nas_eth,neo_eth,ngc_eth,nuls_eth,oax_eth,of_eth,omg_eth,ost_eth,pay_eth,poe_eth,ppt_eth,pra_eth,pst_eth,qtum_eth,qun_eth,qvt_eth,rcn_eth,rct_eth,rdn_eth,read_eth,ref_eth,req_eth,rnt_eth,salt_eth,san_eth,show_eth,smt_eth,snc_eth,sngls_eth,snm_eth,snt_eth,spf_eth,ssc_eth,stc_eth,storj_eth,sub_eth,swftc_eth,tct_eth,theta_eth,tio_eth,tnb_eth,topc_eth,true_eth,trx_eth,ubtc_eth,ugc_eth,ukg_eth,utk_eth,vee_eth,vib_eth,viu_eth,wrc_eth,wtc_eth,xmr_eth,xuc_eth,yee_eth,yoyo_eth,zec_eth,zrx_eth'
# okexSymbol = okexSymbolValue.split(',')
#
# from multiprocessing import Pool
#
#
# if __name__ == '__main__':
#     with Pool(2) as p:
#         print(p.map(save_csv_get_depth, okexSymbol))
#
#



