# Stored Procedure: `sp_KSTC_CheckSynData_MuaNgoai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-05-20 16:21:14.550000
- **Ngày sửa cuối**: 2021-05-31 10:57:44.807000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_KSTC_CheckSynData_MuaNgoai]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	--1. Dự toán mua
	
	Select 'DuToanMua'Loai, Nguon.*,Dich.* from 
	(select ct.Contract_Id, b.PhanBoId,ct.Product_id, a.Id,a.DonGiaMua ,a.SoLuongMua, a.ChietKhauMua,a.PhaiTraNhaCungCap,a.ThanhTienSauCK,a.IsDeleted, a.LastModificationTime ,ct.Last_Modified_At 
	from [asd14].PMS.dbo.B_DuToan_Chitiet_HopDong a inner join
	 [asd14].PMS.dbo.B_DuToan_ChiTiet b on a.B_DuToan_ChiTiet_REF = b.Id
	 left join [asd14].contract.dbo.contract_details ct on ct.Id = b.PhanBoId
	 where  1=1 and a.IsDeleted = 0 and ct.Deleted_Status = 0
	 and ct.Contract_id not in (Select Id from [asd14].contract.dbo.contracts where Status = 3)
	 and b.PhanBoId  in (select PhanBoID from  [asd14].PMS.dbo.B_QuanLyThucChay where IsDeleted = 0)
	 and ( (ct.PRODUCT_FORMALITY_ID = 13) OR 
				 (EXISTS (SELECT a.CONTRACT_DETAIL_ID 
				   FROM [asd14].CONTRACT.dbo.CONTRACT_DETAIL_PRODUCT_PROPERTIES a 
				   WHERE a.PRODUCT_CONFIG_PROPERTY_ID = 5 
				   AND a.VALUE = 18 
				   AND a.DELETED_STATUS = 0 
				   AND a.CONTRACT_DETAIL_ID = ct.ID)
				 )
				) 
	 --and b.PhanBoId =574179
	--and ct.Last_Modified_At <'2020-06-23'
	--and ct.Contract_Id = 1022585
	) 
	Nguon
	full outer join
	(SELECT HopDongFK, mn.HopDongChiTietID,DmSanPhamREF, DonGiaMua, SoLuongMua, ThanhTienSauCKMua, ThanhTienBanSauCK, ThanhTienLaiSauCK
	FROM dbo.HopDongChiTiet_MuaNgoai mn left join HopDongChiTiet b on mn.HopDongChiTietID = b.HopDongChiTietID
	WHERE mn.DeletedStatus = 0 and b.DeletedStatus = 0 and mn.HopDongChiTietID not in ( 529886,532414,549887--hd cũ)
	)
	and (b.DmLoaiREF = 13 or b.DmLoaiBannerREF = 18)
	 and b.HopDongFK not in (Select HopDongID from HopDong where TrangThaiHopDong = 3)
	 and b.HopDongChiTietID  in (select HopDongChiTietREF from  ThucChayMuaNgoaiChiTiet where DeletedStatus = 0)
	
	) Dich
	on Nguon.PhanBoId =Dich.HopDongChiTietID
	where Nguon.PhanBoId  is null or Dich.HopDongChiTietID is null
    -- Insert statements for procedure here
	--2. Thực chạy mua 
 --0 : mới,1: gửi duyệt;2 duyệt thanh toán, 3 -- gửi duyệt thực chạy, --4 duyệt thực chạy
select 'ThucChayMua' Loai, A.Id,B.ThucChayMuaNgoaiChiTietID IdDich
,A.HopDongID,B.HopDongREF
,A.PhanBoId,B.HopDongChiTietREF,B.DmSanPhamREF
,A.ChietKhauMua,B.ChietKhauMuaNgoai
--,(A.ChietKhauMua-B.ChietKhauMuaNgoai)lechck
,A.SoLuongChay,B.SoLuongThucChay
,A.ThanhTien,B.ThanhTienMuaNgoaiTruocCK
,(A.ThanhTien-B.ThanhTienMuaNgoaiTruocCK)lechtien
,A.TrangThai,B.TrangThaiDuyet
,A.IsDeleted,B.DeletedStatus
,A.CreationTime
,A.LastModificationTime,B.LastModifiedAt
--,A.NgayChot, B.NgayChot
from (
select a.Id, a.HopDongID, a.PhanBoId, a.ChietKhauMua, a.SoLuongChay,a.DonGia, a.D_DonViTinhREF, a.ThanhTien, a.IsDeleted,a.TrangThai,a.CreationTime, a.LastModificationTime
--,a.NgayChot
from [asd14].pms.dbo.B_QuanLyThucChay a left join [asd14].contract.dbo.contracts ct on a.HopDongID = ct.Id 
where 1=1 
and ct.[Status] <> 3
AND isnull(a.LastModificationTime,'2013-01-01') >='2020-01-01'
--and a.DonGia <> 0
and a.PhanBoId not in (575154,575112--pbo xử lý riêng
)
--and IsDeleted =0
)A

full outer join 
(
SELECT  ThucChayMuaNgoaiChiTietID,HopDongREF,HopDongChiTietREF, DmSanPhamREF,tc.ChietKhauMuaNgoai,tc.SoLuongThucChay,ThanhTienMuaNgoaiTruocCK,tc.DeletedStatus,[Status] TrangThaiDuyet,tc.LastModifiedAt
 FROM dbo.ThucChayMuaNgoaiChiTiet tc 
 left join HopDongChiTiet dtb on  tc.HopDongChiTietREF = dtb.HopDongChiTietID and dtb.DeletedStatus = 0 and (DmLoaiREF = 13 or DmLoaiBannerREF =18)
 left join HopDong hd on hd.HopDongID = tc.HopDongREF 
WHERE 1= 1  
and hd.TrangThaiHopDong <> 3
AND isnull(tc.LastModifiedAt,'2013-01-01') >='2020-01-01'
--AND ( ( tc.ThanhTienMuaNgoaiTruocCK*(100-tc.ChietKhauMuaNgoai)/100 <> 0 and tc.ChietKhauMuaNgoai <> 100) -- khong check voi tc mua = 0
--or ( tc.ThanhTienMuaNgoaiTruocCK*(100-tc.ChietKhauMuaNgoai)/100 = 0 and tc.ChietKhauMuaNgoai = 100) )
--AND tc.DeletedStatus=0
AND tc.HopDongChiTietREF not in  (575154,575112--pbo xử lý riêng
)

)B
on A.Id = B.ThucChayMuaNgoaiChiTietID
where 1=1
and not (A.IsDeleted =1 and B.DeletedStatus =1 )
and (
A.HopDongID <> B.HopDongREF or A.HopDongID is null or B.HopDongREF is null
or A.PhanBoId <> B.HopDongChiTietREF or A.PhanBoId is null or B.HopDongChiTietREF is null
or A.TrangThai <> B.TrangThaiDuyet or A.TrangThai is null or B.TrangThaiDuyet is null
--or round(A.ChietKhauMua,4) <> round(B.ChietKhauMuaNgoai,4)
or abs (isnull(A.ThanhTien,0) - isnull(B.ThanhTienMuaNgoaiTruocCK,0)) >5
or A.IsDeleted <> B.DeletedStatus

)
order by A.LastModificationTime desc
END

/*
select * from [asd14].pms.dbo.B_QuanLyThucChay where PhanBoId= 527102

select * from ThucChayMuaNgoaiChiTiet where HopDongChiTietREF= 527102
*/
```
