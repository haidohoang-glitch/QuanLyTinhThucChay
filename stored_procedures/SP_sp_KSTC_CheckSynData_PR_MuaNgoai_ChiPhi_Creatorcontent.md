# Stored Procedure: `sp_KSTC_CheckSynData_PR_MuaNgoai_ChiPhi_Creatorcontent`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-12-30 13:51:40.517000
- **Ngày sửa cuối**: 2021-12-30 16:22:40.380000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_KSTC_CheckSynData_PR_MuaNgoai_ChiPhi_Creatorcontent]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

-----1. Check đầu vào đăng tin

EXEC dbo.sp_KSTC_CheckSynData_ThucTreoPR_v2


-----2. Check đầu vào mua ngoài

EXEC dbo.sp_KSTC_CheckSynData_MuaNgoai_v2


----3. Check treo chi phí

EXEC [dbo].[sp_KSTC_CheckSynData_ThucTreoChiPhi_v2]


---4. Check đầu vào GGFB

exec dbo.sp_KSTC_CheckSynData_GGFB


----5. Check đầu vào creatorcontent

SELECT N'CreatorContent' as CheckSynData_CreatorContent, A.*,B.* FROM
(SELECT a.Id, a.HopDongBanRef,a.PhanBoRef, a.PbSoLuong, a.pbDonGia,a.PbChietKhau, a.PbThanhTien, a.TcSoLuong, a.TcDonGia, a.TcThanhTien,a.DonGia, a.ChietKhau, a.ThanhTien, a.IsDeleted,a.TrangThai,a.CreationTime, a.LastModificationTime
FROM ASDAG2.AbpZeroDb_SanPham_CreatorContent.dbo.AppKetQuaVanHanh a
JOIN ASDAG2.CONTRACT.dbo.CONTRACTS b ON a.HopDongBanRef = b.ID
WHERE  CONVERT(DATE,b.INDEXED_DATE) >= '2021-10-01' AND a.TrangThai NOT IN(1,2,4) AND IsDeleted=0 AND a.CreationTime <CONVERT(DATE,GETDATE()) 
--and CONVERT(DATE,a.LastModificationTime) = '2021-10-28' 
) A --truyền vào ngày n-1
FULL OUTER JOIN
(SELECT a.AppKetQuaVanHanh_CreatorContent_id, a.HopDongBanRef, a.PhanBoRef, a.PbSoLuong, a.pbDonGia, a.PbThanhTien, a.TcSoLuong, a.TcDonGia, a.TcThanhTien, a.DonGia, a.ChietKhau, a.ThanhTien, a.IsDeleted, a.TrangThai, a.CreationTime, a.LastModificationTime 
FROM ABM_Data_ThucChay.dbo.AppKetQuaVanHanh_CreatorContent a
JOIN ABM_Data_ThucChay.dbo.HopDong b ON b.HopDongID = a.HopDongBanRef
WHERE TrangThai NOT IN(1,2,4) AND IsDeleted=0 AND CONVERT(DATE,b.NgayDanhSoHopDong) >= '2021-10-01' AND a.CreationTime <CONVERT(DATE,GETDATE())
) B--truyền vào ngày n-1
ON A.PhanBoRef = B.PhanBoRef
WHERE A.Id IS NULL OR B.AppKetQuaVanHanh_CreatorContent_id IS NULL
OR A.HopDongBanRef <> B.HopDongBanRef 
OR A.PhanBoRef <> B.PhanBoRef
OR A.PbSoLuong <> B.PbSoLuong
OR A.pbDonGia <> B.pbDonGia
OR A.ChietKhau <> B.ChietKhau
ORDER BY A.LastModificationTime,B.LastModificationTime DESC
	
END

```
