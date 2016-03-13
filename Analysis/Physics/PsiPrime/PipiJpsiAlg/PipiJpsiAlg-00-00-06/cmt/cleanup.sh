if test "${CMTROOT}" = ""; then
  CMTROOT=/afs/ihep.ac.cn/bes3/offline/ExternalLib/contrib/CMT/v1r20p20081118; export CMTROOT
fi
. ${CMTROOT}/mgr/setup.sh
tempfile=`${CMTROOT}/mgr/cmt -quiet build temporary_name`
if test ! $? = 0 ; then tempfile=/tmp/cmt.$$; fi
${CMTROOT}/mgr/cmt cleanup -sh -pack=PipiJpsiAlg -version=PipiJpsiAlg-00-00-06 -path=/afs/ihep.ac.cn/users/s/shixin/bes/jpsi2invi/v0.1/Analysis/Physics/PsiPrime $* >${tempfile}; . ${tempfile}
/bin/rm -f ${tempfile}
